import time
import os
import sys
import re
import datetime
import difflib
import subprocess

# Configuration
MD_FILE = 'index.md'
HTML_FILE = 'index.html'

def get_mtime(path):
    return os.stat(path).st_mtime

def minify_html(content):
    # Markers to identify the markdown block which must NOT be minified
    start_marker = '<script type="text/template" id="markdown-source">'
    end_marker = '</script>'
    
    # Split content by the markdown block to protect it
    pattern = re.compile(f'({re.escape(start_marker)}.*?{re.escape(end_marker)})', re.DOTALL)
    parts = pattern.split(content)
    
    minified_parts = []
    for part in parts:
        if part.startswith(start_marker):
            # Keep markdown block exactly as is
            minified_parts.append(part)
        else:
            # Minify HTML parts
            # 1. Remove HTML comments
            part = re.sub(r'<!--(?!\[if).*?-->', '', part, flags=re.DOTALL)
            # 2. Remove whitespace between tags
            part = re.sub(r'>\s+<', '><', part)
            minified_parts.append(part.strip())
            
    return ''.join(minified_parts)

def get_slug(title):
    # Clean title: remove markdown links and special chars to match likely ID
    clean_title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', title)
    clean_title = re.sub(r'[^\w\s-]', '', clean_title)
    slug = clean_title.lower().strip().replace(' ', '-')
    slug = re.sub(r'-+', '-', slug)
    return slug

def validate_internal_links(md_content):
    print("Validating internal links...")
    # Strip front matter
    content = re.sub(r'^---[\s\S]*?---\n', '', md_content)
    
    # 1. Collect valid IDs from headers
    headers = re.findall(r'^(#{2,3})\s+(.+)$', content, re.MULTILINE)
    valid_ids = set()
    valid_ids.add('top') # Common manual anchor
    valid_ids.add('table-of-contents') # Common manual anchor
    
    for _, title in headers:
        slug = get_slug(title)
        if slug:
            valid_ids.add(slug)
            
    # 2. Find and check links
    links = re.findall(r'\[([^\]]+)\]\(#([^\)]+)\)', content)
    broken_count = 0
    
    for text, link in links:
        if link not in valid_ids:
            print(f"⚠️  Broken link detected: [{text}](#{link}) - Target header not found.")
            broken_count += 1
            
    if broken_count > 0:
        print(f"❌ Found {broken_count} broken internal links.")
        return False
    return True

def fix_broken_links(content):
    print("Checking for broken links to fix...")
    # 1. Extract all headers and generate valid slugs map
    headers = re.findall(r'^(#{2,3})\s+(.+)$', content, re.MULTILINE)
    valid_slugs = {}
    for _, title in headers:
        slug = get_slug(title)
        if slug:
            valid_slugs[slug] = title
    
    # Add manual anchors
    valid_slugs['top'] = "Top"
    valid_slugs['table-of-contents'] = "Table of Contents"
    
    changes_made = False
    
    # 2. Fix Markdown Links: [text](#slug)
    def replace_link(match):
        nonlocal changes_made
        text = match.group(1)
        slug = match.group(2)
        
        if slug in valid_slugs:
            return match.group(0)
        
        # Attempt fix: Fuzzy match slug against valid slugs
        matches = difflib.get_close_matches(slug, valid_slugs.keys(), n=1, cutoff=0.6)
        if matches:
            best_match = matches[0]
            print(f"🔧 Fixed link: [{text}](#{slug}) -> (#{best_match})")
            changes_made = True
            return f"[{text}](#{best_match})"
        
        return match.group(0)
    
    new_content = re.sub(r'\[([^\]]+)\]\(#([^\)]+)\)', replace_link, content)
    
    # 3. Fix HTML Links: href="#slug"
    def replace_html_link(match):
        nonlocal changes_made
        slug = match.group(1)
        if slug in valid_slugs: return match.group(0)
        
        matches = difflib.get_close_matches(slug, valid_slugs.keys(), n=1, cutoff=0.6)
        if matches:
            print(f"🔧 Fixed HTML link: href=\"#{slug}\" -> href=\"#{best_match}\"")
            changes_made = True
            return f'href="#{matches[0]}"'
        return match.group(0)

    new_content = re.sub(r'href="#([^"]+)"', replace_html_link, new_content)
    return new_content, changes_made

def generate_sitemap(md_content):
    print("Generating sitemap.xml...")
    base_url = "https://kamalsoft.github.io/macOS-cheat-sheet/"
    
    # Strip front matter for processing
    content = re.sub(r'^---[\s\S]*?---\n', '', md_content)
    
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # Main URL
    lastmod = datetime.datetime.now().strftime("%Y-%m-%d")
    sitemap.append(f'  <url>\n    <loc>{base_url}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>')
    
    # Headers (## and ###)
    headers = re.findall(r'^(#{2,3})\s+(.+)$', content, re.MULTILINE)
    
    for _, title in headers:
        slug = get_slug(title)
        
        if slug:
            sitemap.append(f'  <url>\n    <loc>{base_url}#{slug}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.5</priority>\n  </url>')
            
    sitemap.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap))

def update_toc(content):
    print("Checking Table of Contents...")
    # Strip front matter for header search to avoid confusion
    body_content = re.sub(r'^---[\s\S]*?---\n', '', content)
    headers = re.findall(r'^(#{2,3})\s+(.+)$', body_content, re.MULTILINE)
    
    toc_lines = ["## 📋 Table of Contents", ""]
    has_toc_header = False
    
    for level, title in headers:
        if "Table of Contents" in title:
            has_toc_header = True
            continue
        if "Related Topics" in title:
            continue
        
        slug = get_slug(title)
        indent = "  " if level == "###" else ""
        toc_lines.append(f"{indent}* [{title}](#{slug})")
    
    toc_block = "\n".join(toc_lines) + "\n"
    
    if has_toc_header:
        # Replace existing TOC section (assuming it ends at the next horizontal rule or header)
        pattern = r'(## 📋 Table of Contents)([\s\S]*?)(?=\n---|(?:\n#{2,3} )|$)'
        if re.search(pattern, content):
            new_content = re.sub(pattern, toc_block, content, count=1)
            if new_content != content:
                print("Updating Table of Contents in markdown...")
                return new_content, True
    else:
        # Insert TOC if missing
        print("Generating missing Table of Contents...")
        # Find the first H2 to insert before
        match = re.search(r'^(#{2,3} )', content, re.MULTILINE)
        if match:
            start = match.start()
            new_content = content[:start] + toc_block + "\n---\n\n" + content[start:]
            return new_content, True
            
    return content, False

def update_changelog(content):
    print("Updating Changelog...")
    try:
        # Get git history
        # We use git log to get the last 5 commits affecting index.md
        cmd = ['git', 'log', '-n', '5', '--date=short', '--pretty=format:- **%ad**: %s', 'index.md']
        history = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8').strip()
        
        if not history:
            return content, False

        changelog_block = "## 🆕 New & Updated\n\n" + history + "\n"
        
        # Check if section exists and replace it
        pattern = r'(## 🆕 New & Updated)([\s\S]*?)(?=\n---|(?:\n#{2,3} )|$)'
        if re.search(pattern, content):
            new_content = re.sub(pattern, changelog_block, content, count=1)
            if new_content != content:
                return new_content, True
        else:
            # Insert after TOC if it exists
            toc_pattern = r'(## 📋 Table of Contents)([\s\S]*?)(?=\n---|(?:\n#{2,3} )|$)'
            match = re.search(toc_pattern, content)
            if match:
                end_pos = match.end()
                new_content = content[:end_pos] + "\n\n---\n\n" + changelog_block + content[end_pos:]
                return new_content, True
                
        return content, False
    except Exception as e:
        print(f"Warning: Could not update changelog (git error?): {e}")
        return content, False

def generate_related_topics(md_content):
    print("Generating Related Topics...")
    
    # 1. Parse Sections
    lines = md_content.split('\n')
    sections = []
    current_section_lines = []
    current_title = "Intro"
    
    for line in lines:
        if line.startswith("## ") and not line.startswith("###"):
            sections.append({'title': current_title, 'lines': current_section_lines})
            current_title = line[3:].strip()
            current_section_lines = [line]
        else:
            current_section_lines.append(line)
    sections.append({'title': current_title, 'lines': current_section_lines})
    
    # 2. Extract Keywords
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'else', 'when', 'at', 'by', 'for', 'with', 
        'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 
        'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 
        'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
        'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 
        'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',
        'mac', 'macos', 'apple', 'use', 'using', 'guide', 'install', 'free', 'paid', 'open', 'source',
        'version', 'update', 'upgrade', 'check', 'click', 'press', 'type', 'select', 'enable', 'disable',
        'feature', 'support', 'system', 'tool', 'app', 'application', 'software', 'command', 'terminal',
        'setup', 'config', 'configuration', 'best', 'top', 'list', 'level', 'pro', 'max', 'mini', 'air',
        'intro', 'table', 'contents', 'new', 'updated', 'resources', 'related', 'topics'
    }
    
    section_keywords = {}
    ignored_titles = ["Table of Contents", "New & Updated", "Best Resources by Level", "Intro"]
    
    for i, sec in enumerate(sections):
        title = sec["title"]
        if any(ignored in title for ignored in ignored_titles):
            continue
            
        text = " ".join(sec["lines"]).lower()
        text = re.sub(r'[#*`\[\]\(\)!:;,.?]', ' ', text)
        words = re.findall(r'\b[a-z]{3,}\b', text)
        keywords = set([w for w in words if w not in stop_words])
        section_keywords[i] = keywords

    # 3. Calculate Similarity
    related_map = {}
    for i in section_keywords:
        scores = []
        for j in section_keywords:
            if i == j: continue
            s1 = section_keywords[i]
            s2 = section_keywords[j]
            if not s1 or not s2: continue
            intersection = len(s1.intersection(s2))
            union = len(s1.union(s2))
            score = intersection / union if union > 0 else 0
            if score > 0.08:
                scores.append((score, j))
        scores.sort(key=lambda x: x[0], reverse=True)
        related_map[i] = [x[1] for x in scores[:3]]

    # 4. Reconstruct Content
    new_lines = []
    for i, sec in enumerate(sections):
        lines = sec["lines"]
        cleaned_lines = []
        skip = False
        for line in lines:
            if "### 🔗 Related Topics" in line: skip = True
            elif skip and (line.startswith("## ") or line.strip() == "---" or line.startswith("[↑ Back to Top]")):
                skip = False; cleaned_lines.append(line)
            elif not skip: cleaned_lines.append(line)
            
        if i in related_map and related_map[i]:
            insert_idx = len(cleaned_lines)
            for idx in range(len(cleaned_lines) - 1, -1, -1):
                line = cleaned_lines[idx].strip()
                if line == "---" or line.startswith("[↑ Back to Top]"): insert_idx = idx
                elif line != "": break
            
            related_block = ["", "### 🔗 Related Topics", ""]
            for related_idx in related_map[i]:
                related_title = sections[related_idx]["title"]
                slug = get_slug(related_title)
                related_block.append(f"- {related_title}")
            related_block.append("")
            cleaned_lines[insert_idx:insert_idx] = related_block
            
        new_lines.extend(cleaned_lines)
        
    return "\n".join(new_lines)

def compress_images(md_content):
    print("Checking for images to compress...")
    try:
        from PIL import Image
        import io
    except ImportError:
        print("Warning: PIL (Pillow) not installed. Skipping image compression.")
        return

    # Regex for markdown images: ![alt](path)
    md_images = re.findall(r'!\[.*?\]\((?!http)(.*?)\)', md_content)
    # Regex for HTML images: <img src="path">
    html_images = re.findall(r'<img.*?src=["\'](?!http)(.*?)["\']', md_content)
    
    all_images = set(md_images + html_images)
    
    for img_path in all_images:
        # Clean path (remove query/hash)
        # Also remove markdown titles: path/to/image.png "Title"
        clean_path = img_path.strip()
        if ' ' in clean_path:
            clean_path = clean_path.split(' ')[0]
        clean_path = clean_path.split('?')[0].split('#')[0]
        
        if not os.path.exists(clean_path):
            continue
            
        try:
            current_size = os.path.getsize(clean_path)
            with Image.open(clean_path) as img:
                if not img.format: continue
                
                buffer = io.BytesIO()
                img.save(buffer, format=img.format, optimize=True, quality=85)
                new_size = buffer.tell()
                
                if new_size < current_size:
                    with open(clean_path, 'wb') as f:
                        f.write(buffer.getvalue())
                    print(f"Compressed {clean_path}: {current_size} -> {new_size} bytes")
        except Exception as e:
            print(f"Error compressing {clean_path}: {e}")

def generate_command_index(md_content):
    print("Generating commands.json...")
    import json
    
    # Find code blocks
    # Regex for ```lang ... ```
    blocks = re.findall(r'```(\w+)\n(.*?)```', md_content, re.DOTALL)
    
    commands = []
    for lang, code in blocks:
        if lang in ['bash', 'sh', 'zsh', 'shell']:
            lines = code.strip().split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'): continue
                # Remove leading $ if present
                cmd = re.sub(r'^\$\s+', '', line)
                commands.append({'cmd': cmd, 'lang': lang})
                
    with open('commands.json', 'w', encoding='utf-8') as f:
        json.dump(commands, f, indent=2)

def fix_markdown_linting(content):
    print("Fixing common markdown linting errors...")
    
    # 1. Fix trailing whitespace on lines
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # 2. Fix multiple consecutive blank lines (max 1 blank line = 2 newlines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 3. Ensure space after list markers (e.g., "-Item" -> "- Item")
    content = re.sub(r'^(\s*[-*])([^\s])', r'\1 \2', content, flags=re.MULTILINE)
    
    # 4. Ensure blank lines before headers (if not already present)
    # Matches a non-newline char, followed by newline, followed by header
    content = re.sub(r'([^\n])\n(\#{1,6} )', r'\1\n\n\2', content)
    
    return content

def update_html():
    print(f"Change detected. Updating {HTML_FILE} from {MD_FILE}...")
    try:
        with open(MD_FILE, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Fix Linting Errors
        md_content = fix_markdown_linting(md_content)

        # Update TOC in Markdown if needed
        md_content, updated = update_toc(md_content)
        
        # Update Changelog
        md_content, log_updated = update_changelog(md_content)
        
        # Generate Related Topics
        new_md_content = generate_related_topics(md_content)
        related_updated = new_md_content != md_content
        md_content = new_md_content
        
        # Compress Images
        compress_images(md_content)
        
        # Generate Command Index
        generate_command_index(md_content)
        
        # Fix broken links
        md_content, fixed = fix_broken_links(md_content)
        
        if updated or fixed or log_updated or related_updated:
            with open(MD_FILE, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
        # Validate Links before proceeding
        if not validate_internal_links(md_content):
            print("Warning: Broken links detected. Proceeding with update anyway.")

        # Markers to identify the injection point
        start_marker = '<script type="text/template" id="markdown-source">'
        end_marker = '</script>'
        
        start_idx = html_content.find(start_marker)
        if start_idx == -1:
            print(f"Error: Start marker '{start_marker}' not found in {HTML_FILE}")
            return

        # Calculate where the content starts (after the opening tag)
        content_start = start_idx + len(start_marker)
        
        # Find the closing script tag after the content start
        # We assume the next </script> is the closing tag for our template
        end_idx = html_content.find(end_marker, content_start)
        
        if end_idx == -1:
            print(f"Error: End marker '{end_marker}' not found in {HTML_FILE}")
            return
            
        # Construct new HTML content
        # We add a newline before and indentation before the closing tag for formatting
        new_html = html_content[:content_start] + '\n' + md_content + '\n    ' + html_content[end_idx:]
        
        # Update Timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts_div = f'<div id="build-timestamp" class="text-center text-xs text-slate-400 dark:text-slate-500 mt-12 mb-6">Last updated: {timestamp}</div>'
        new_html = re.sub(r'<div id="build-timestamp".*?</div>', ts_div, new_html, flags=re.DOTALL)

        # Minify the output
        new_html = minify_html(new_html)
        
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        # Generate Sitemap
        generate_sitemap(md_content)
            
        print("Update successful.")
        
    except Exception as e:
        print(f"Error updating file: {e}")

def watch():
    if not os.path.exists(MD_FILE) or not os.path.exists(HTML_FILE):
        print(f"Error: Ensure both {MD_FILE} and {HTML_FILE} exist in the current directory.")
        return

    print(f"Watching {MD_FILE} for changes... (Press Ctrl+C to stop)")
    last_mtime = get_mtime(MD_FILE)
    
    try:
        while True:
            time.sleep(1)
            current_mtime = get_mtime(MD_FILE)
            if current_mtime != last_mtime:
                last_mtime = current_mtime
                update_html()
    except KeyboardInterrupt:
        print("\nStopping watcher.")

if __name__ == "__main__":
    # Usage: python3 update_site.py [once]
    if len(sys.argv) > 1 and sys.argv[1] == 'once':
        update_html()
    else:
        watch()