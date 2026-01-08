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
        clean_path = img_path.split('?')[0].split('#')[0]
        
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

def update_html():
    print(f"Change detected. Updating {HTML_FILE} from {MD_FILE}...")
    try:
        with open(MD_FILE, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Update TOC in Markdown if needed
        md_content, updated = update_toc(md_content)
        
        # Update Changelog
        md_content, log_updated = update_changelog(md_content)
        
        # Compress Images
        compress_images(md_content)
        
        # Fix broken links
        md_content, fixed = fix_broken_links(md_content)
        
        if updated or fixed or log_updated:
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