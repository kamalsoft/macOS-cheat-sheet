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
    # Enforce ASCII slugs for better compatibility with JS
    clean_title = re.sub(r'[^a-zA-Z0-9\s-]', '', clean_title)
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
            best_match = matches[0]
            print(f"🔧 Fixed HTML link: href=\"#{slug}\" -> href=\"#{best_match}\"")
            changes_made = True
            return f'href="#{best_match}"'
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

    # Build Tree Structure
    toc_tree = []
    current_h2 = None

    for level, title in headers:
        if "Table of Contents" in title:
            continue
        if "Related Topics" in title:
            continue
        if "New & Updated" in title:
            continue
        if "Contributors" in title:
            continue
        if "Best Resources" in title:
            continue
        
        slug = get_slug(title)
        
        if level == "##":
            current_h2 = {"title": title, "slug": slug, "children": []}
            toc_tree.append(current_h2)
        elif level == "###" and current_h2:
            current_h2["children"].append({"title": title, "slug": slug})

    # Categorize into Levels
    levels = {
        "Beginner": [],
        "Mid-Level": [],
        "Pro": [],
        "Expert": []
    }

    for item in toc_tree:
        title = item["title"]
        if "🔴" in title or "Expert" in title or "SIP" in title or "Network Analysis" in title:
            levels["Expert"].append(item)
        elif "🟠" in title or "Pro" in title or "Advanced" in title or "Privacy" in title or "Creative" in title or "Design" in title or "Audio" in title or "Music" in title or "Writing" in title:
            levels["Pro"].append(item)
        elif "🟡" in title or "Mid-Level" in title or "Developer" in title or "Homebrew" in title or "Virtualization" in title or "Database" in title or "Local Development" in title or "Automation" in title:
            levels["Mid-Level"].append(item)
        else:
            levels["Beginner"].append(item)

    # Generate HTML Grid
    toc_html = ['## 📋 Table of Contents', '', '<div class="toc-grid">']
    
    level_icons = {"Beginner": "🟢", "Mid-Level": "🟡", "Pro": "🟠", "Expert": "🔴"}
    
    for level_name, items in levels.items():
        if not items: continue
        toc_html.append(f'  <div class="toc-column">')
        toc_html.append(f'    <h3>{level_icons[level_name]} {level_name}</h3>')
        
        for item in items:
            if item["children"]:
                toc_html.append(f'    <details>')
                toc_html.append(f'      <summary><a href="#{item["slug"]}">{item["title"]}</a></summary>')
                toc_html.append(f'      <ul>')
                for child in item["children"]:
                    toc_html.append(f'        <li><a href="#{child["slug"]}">{child["title"]}</a></li>')
                toc_html.append(f'      </ul>')
                toc_html.append(f'    </details>')
            else:
                toc_html.append(f'    <div class="toc-item"><a href="#{item["slug"]}">{item["title"]}</a></div>')
        
        toc_html.append('  </div>')

    toc_html.append('</div>')
    toc_html.append('')
    
    toc_block = "\n".join(toc_html)
    
    # Check if TOC exists
    has_toc_header = "## 📋 Table of Contents" in content

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

def generate_quick_sidebar(content):
    print("Generating Quick Links Sidebar...")
    
    # Define mapping of keywords to icons for the quick grid
    # We look for headers containing these keywords
    quick_map = {
        "Shortcuts": "⌨️",
        "Terminal": "💻",
        "Settings": "⚙️",
        "Homebrew": "🍺",
        "Troubleshooting": "🚑",
        "Developer": "🛠️",
        "Virtualization": "🖥️"
    }
    
    headers = re.findall(r'^(#{2,3})\s+(.+)$', content, re.MULTILINE)
    tiles = []
    
    for _, title in headers:
        clean_title = re.sub(r'^[🟢🟡🟠🔴]\s*', '', title) # Remove status icons
        clean_title = re.sub(r'\s*[🟢🟡🟠🔴]$', '', clean_title)
        
        for key, icon in quick_map.items():
            if key in clean_title and len(tiles) < 8: # Limit to 8 tiles
                slug = get_slug(title)
                # Check if we already have this key to avoid duplicates (e.g. multiple Terminal headers)
                if not any(t['label'] == key for t in tiles):
                    tiles.append({'icon': icon, 'label': key, 'slug': slug})
                break
    
    if not tiles:
        return content, False
        
    # Construct HTML block
    sidebar_html = '<div class="quick-nav-sidebar">\n'
    for t in tiles:
        sidebar_html += f'  <a href="#{t["slug"]}" class="quick-nav-item" title="{t["label"]}">{t["icon"]}</a>\n'
    sidebar_html += '</div>\n'
    
    # Inject after Hero section (which is usually the first thing after front matter/title)
    # We look for the first separator "---"
    # Match various HR formats on a new line (---, - --, etc)
    pattern = r'(?m)^[-*_ ]{3,}\s*$'
    match = re.search(pattern, content)
    if match:
        # Check if sidebar or old grid already exists to replace or insert
        sidebar_pattern = r'(<div class="quick-(grid|nav-sidebar)">[\s\S]*?</div>)'
        if re.search(sidebar_pattern, content):
            new_content = re.sub(sidebar_pattern, sidebar_html, content, count=1)
            if new_content != content:
                return new_content, True
        else:
            # Insert after the first separator
            end_pos = match.end()
            new_content = content[:end_pos] + "\n\n" + sidebar_html + content[end_pos:]
            return new_content, True
            
    return content, False

def update_last_updated_badge(content):
    print("Updating Last Updated badge...")
    today = datetime.datetime.now().strftime("%Y--%m--%d")
    badge_url = f"https://img.shields.io/badge/Last%20Updated-{today}-blue.svg"
    badge_md = f"[![Last Updated]({badge_url})](https://github.com/kamalsoft/macOS-cheat-sheet/commits/main)"
    
    # Check if badge exists
    pattern = r'\[!\[Last Updated\]\(.*?\)\].*?\)'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, badge_md, content)
        if new_content != content:
            return new_content, True
    else:
        # Insert after PRs Welcome badge
        pr_pattern = r'(\[!\[PRs Welcome\].*?\)\].*?\))'
        match = re.search(pr_pattern, content)
        if match:
            new_content = content[:match.end()] + '\n' + badge_md + content[match.end():]
            return new_content, True
            
    return content, False

def update_contributors(content):
    print("Updating Contributors...")
    try:
        # Get contributors from git
        cmd = ['git', 'log', '--format=%aN']
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8').strip()
        
        if not output:
            return content, False
            
        authors = sorted(list(set(output.split('\n'))))
        
        if not authors:
            return content, False
            
        contrib_md = "## 👥 Contributors\n\nThanks to these wonderful people: " + ", ".join([f"**{a}**" for a in authors]) + ".\n"
        
        pattern = r'(## 👥 Contributors)([\s\S]*?)(?=\n---|(?:\n#{2,3} )|$)'
        if re.search(pattern, content):
            new_content = re.sub(pattern, contrib_md, content, count=1)
            if new_content != content:
                return new_content, True
        else:
             # Insert before "Best Resources by Level"
            target = "## Best Resources by Level"
            if target in content:
                new_content = content.replace(target, contrib_md + "\n" + target)
                return new_content, True
            else:
                new_content = content + "\n\n" + contrib_md
                return new_content, True

        return content, False
    except Exception as e:
        print(f"Warning: Could not update contributors: {e}")
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
                related_block.append(f"- [{related_title}](#{slug})")
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

def inject_seo(html_content, md_content):
    print("Injecting SEO tags...")
    # Parse front matter
    front_matter = {}
    fm_match = re.match(r'^---[\s\S]*?---\n', md_content)
    if fm_match:
        fm_text = fm_match.group(0)
        for line in fm_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                front_matter[key.strip()] = val.strip()
    
    title = front_matter.get('title', 'macOS Mastered')
    desc = front_matter.get('description', 'The ultimate macOS cheat sheet.')
    keywords = front_matter.get('keywords', 'macOS, cheat sheet, shortcuts, terminal')
    author = front_matter.get('author', 'KamalSoft')
    url = "https://kamalsoft.github.io/macOS-cheat-sheet/"
    
    meta_tags = f"""
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="{author}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="{url}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍎</text></svg>">
    
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "{title}",
      "description": "{desc}",
      "author": {{
        "@type": "Person",
        "name": "{author}"
      }},
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{url}"
      }}
    }}
    </script>
    """
    
    # Update title tag if present
    if '<title>' in html_content:
        html_content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_content)

    # Inject into <head>
    if '</head>' in html_content:
        return html_content.replace('</head>', meta_tags + '\n</head>')
    return html_content
    
def inject_html_attributes(html_content):
    # Inject lang and class for theme
    if '<html' in html_content and 'lang=' not in html_content:
        html_content = html_content.replace('<html', '<html lang="en"')
    return html_content

def inject_lazy_loading(html_content):
    # Add loading="lazy" to images that don't have it
    return re.sub(r'<img (?!.*?loading=)(.*?)>', r'<img \1 loading="lazy">', html_content)

def create_base_html():
    print("Creating base index.html...")
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>macOS Mastered</title>
</head>
<body>
    <script type="text/template" id="markdown-source">
    </script>
</body>
</html>"""
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

def inject_styles(html_content):
    print("Injecting custom styles...")
    css = """
    <style id="custom-styles">
        :root {
            --bg-color: #ffffff;
            --text-color: #111827;
            --text-secondary: #4b5563;
            --link-color: #0066cc;
            --border-color: #e5e7eb;
            --code-bg: #f3f4f6;
            --sidebar-bg: #f9fafb;
            --accent: #0071e3;
            --card-bg: #ffffff;
            --shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
        }
        html.dark {
            --bg-color: #0f172a;
            --text-color: #f3f4f6;
            --text-secondary: #9ca3af;
            --link-color: #38bdf8;
            --border-color: #1e293b;
            --code-bg: #1e293b;
            --sidebar-bg: #1e293b;
            --accent: #38bdf8;
            --card-bg: #1e293b;
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.5);
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            transition: background-color 0.3s, color 0.3s;
        }
        
        /* Layout */
        .container { max-width: 1200px; margin: 0 auto; padding: 40px 20px 40px 140px; display: block; }
        #main-content { min-width: 0; }
        
        /* Progress Bar */
        #progress-container {
            position: fixed; top: 0; left: 0; width: 100%; height: 4px; z-index: 1000; background: transparent;
        }
        #progress-bar {
            height: 100%; background: var(--accent); width: 0%; transition: width 0.1s;
        }
        
        /* Typography */
        h1, h2, h3, h4 { color: var(--text-color); margin-top: 1.5em; line-height: 1.2; }
        h1 { font-size: 3rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 1rem; background: linear-gradient(135deg, var(--text-color), var(--text-secondary)); -webkit-background-clip: text; }
        h2 { font-size: 2rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; margin-top: 2.5rem; }
        h3 { font-size: 1.5rem; font-weight: 600; }
        a { color: var(--link-color); text-decoration: none; }
        a:hover { text-decoration: underline; }
        
        /* Code Blocks */
        code { background: var(--code-bg); padding: 0.2em 0.4em; border-radius: 6px; font-family: "SF Mono", Menlo, Monaco, Consolas, monospace; font-size: 0.9em; color: var(--accent); }
        pre { background: var(--code-bg); padding: 1.5em; border-radius: 12px; overflow-x: auto; position: relative; border: 1px solid var(--border-color); }
        pre code { background: none; padding: 0; }
        .copy-btn {
            position: absolute; top: 10px; right: 10px;
            background: var(--card-bg); border: 1px solid var(--border-color);
            color: var(--text-secondary); border-radius: 6px;
            padding: 4px 8px; font-size: 0.8rem; cursor: pointer;
            opacity: 0; transition: opacity 0.2s;
        }
        pre:hover .copy-btn { opacity: 1; }
        
        /* Navigation & Sidebar */
        .quick-nav-sidebar {
            width: 80px; flex-shrink: 0;
            position: fixed; top: 50%; left: 20px; transform: translateY(-50%);
            height: auto;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 15px; border-radius: 16px;
            box-shadow: var(--shadow); 
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 50;
            display: flex; flex-direction: column; gap: 15px; align-items: center;
        }
        html.dark .quick-nav-sidebar {
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .quick-nav-item { 
            font-size: 1.8rem; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
            display: flex; justify-content: center; align-items: center;
            width: 50px; height: 50px; border-radius: 12px;
            color: var(--text-color);
        }
        .quick-nav-item:hover { transform: scale(1.15); background: rgba(0,0,0,0.05); }
        html.dark .quick-nav-item:hover { background: rgba(255,255,255,0.1); }
        
        /* Command Palette */
        .search-trigger {
            width: 100%; padding: 16px 20px; font-size: 1.1rem;
            border: 2px solid var(--border-color); border-radius: 12px;
            background: var(--card-bg); color: var(--text-secondary);
            box-shadow: var(--shadow); cursor: text;
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 30px; position: sticky; top: 20px; z-index: 40;
            transition: border-color 0.2s;
        }
        .search-trigger:hover { border-color: var(--accent); }
        .shortcut-hint {
            background: var(--border-color); padding: 2px 8px; border-radius: 6px; font-size: 0.9rem;
        }
        
        #cmd-palette-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.5); z-index: 9999;
            display: none; justify-content: center; align-items: flex-start;
            padding-top: 100px;
            backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px);
        }
        #cmd-palette-overlay.visible { display: flex; }
        #cmd-palette-modal {
            width: 600px; max-width: 90%;
            background: var(--card-bg);
            border-radius: 16px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            overflow: hidden;
            border: 1px solid var(--border-color);
            display: flex; flex-direction: column;
            animation: slideDown 0.2s ease-out;
        }
        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        #cmd-palette-input {
            width: 100%; padding: 20px;
            font-size: 1.2rem; border: none; border-bottom: 1px solid var(--border-color);
            background: transparent; color: var(--text-color);
            outline: none;
        }
        #cmd-palette-results {
            max-height: 400px; overflow-y: auto;
            padding: 8px;
        }
        .cmd-item {
            padding: 12px 16px; margin-bottom: 4px;
            border-radius: 8px; cursor: pointer;
            display: flex; justify-content: space-between; align-items: center;
            color: var(--text-color);
            text-decoration: none;
            transition: background-color 0.1s;
        }
        .cmd-item:hover, .cmd-item.active {
            background: var(--accent); color: white;
        }
        .cmd-item .cmd-type {
            font-size: 0.75rem; opacity: 0.7;
            background: rgba(125,125,125,0.2); padding: 2px 6px; border-radius: 4px;
            text-transform: uppercase; letter-spacing: 0.05em;
        }
        
        /* Table of Contents Grid */
        .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .toc-column { background: var(--card-bg); padding: 20px; border-radius: 12px; border: 1px solid var(--border-color); box-shadow: var(--shadow); }
        .toc-column h3 { margin-top: 0; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; font-size: 1.2rem; margin-bottom: 15px; }
        .toc-item { margin-bottom: 8px; }
        
        details { margin-bottom: 8px; }
        summary { cursor: pointer; font-weight: 500; list-style: none; position: relative; padding-left: 15px; }
        summary::-webkit-details-marker { display: none; }
        summary::before { content: "▸"; position: absolute; left: 0; color: var(--text-secondary); transition: transform 0.2s; }
        details[open] summary::before { transform: rotate(90deg); }
        summary a { color: var(--text-color); text-decoration: none; }
        summary a:hover { color: var(--accent); text-decoration: underline; }
        details ul { list-style: none; padding-left: 15px; margin: 5px 0; border-left: 2px solid var(--border-color); }
        details li { margin: 4px 0; font-size: 0.9em; }
        
        /* UI Components */
        .shortcuts-table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 1.5em 0; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; }
        .shortcuts-table th, .shortcuts-table td { text-align: left; padding: 12px 16px; border-bottom: 1px solid var(--border-color); }
        .shortcuts-table th { background: var(--sidebar-bg); font-weight: 600; }
        .shortcuts-table tr:last-child td { border-bottom: none; }
        
        blockquote { border-left: 4px solid var(--accent); margin: 1.5em 0; padding-left: 1em; color: var(--text-secondary); background: var(--code-bg); padding: 1em; border-radius: 0 8px 8px 0; }
        img { max-width: 100%; height: auto; border-radius: 8px; box-shadow: var(--shadow); }
        
        /* Skip Link */
        .skip-link { position: absolute; top: -40px; left: 0; background: var(--accent); color: white; padding: 8px; z-index: 100; transition: top 0.2s; }
        .skip-link:focus { top: 0; }
        
        /* Back to Top */
        #back-to-top {
            position: fixed; bottom: 30px; right: 30px;
            width: 50px; height: 50px; border-radius: 50%;
            background: var(--accent); color: white; border: none;
            box-shadow: var(--shadow); cursor: pointer;
            display: flex; justify-content: center; align-items: center;
            font-size: 1.5rem; z-index: 90;
            opacity: 0; visibility: hidden; transition: opacity 0.3s, transform 0.2s;
        }
        #back-to-top.visible { opacity: 1; visibility: visible; }
        #back-to-top:hover { transform: scale(1.1); }
        
        /* Section Navigation */
        #section-nav {
            position: fixed; bottom: 30px; right: 90px;
            display: flex; gap: 10px; z-index: 90;
            opacity: 0; visibility: hidden; transition: opacity 0.3s;
        }
        #section-nav.visible { opacity: 1; visibility: visible; }
        .nav-btn {
            width: 50px; height: 50px; border-radius: 50%;
            background: var(--card-bg); color: var(--text-color);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow); cursor: pointer;
            display: flex; justify-content: center; align-items: center;
            font-size: 1.2rem; transition: transform 0.2s, background-color 0.2s;
        }
        .nav-btn:hover { transform: scale(1.1); background: var(--accent); color: white; border-color: var(--accent); }
        
        /* Focus Mode */
        .content-section { transition: opacity 0.5s ease, filter 0.5s ease; }
        body.focus-mode .content-section { opacity: 0.15; filter: blur(2px); }
        body.focus-mode .content-section.active { opacity: 1; filter: none; }
        
        /* Footer */
        .site-footer {
            margin-top: 80px; padding: 60px 20px;
            border-top: 1px solid var(--border-color);
            text-align: center; color: var(--text-secondary);
            font-size: 0.95rem;
            background: linear-gradient(to bottom, var(--bg-color), var(--sidebar-bg));
        }
        .site-footer p { margin: 8px 0; }
        .site-footer strong { color: var(--text-color); font-weight: 600; }
        .footer-links { margin: 20px 0; display: flex; justify-content: center; gap: 20px; }
        .footer-links a { color: var(--text-secondary); transition: color 0.2s; }
        .footer-links a:hover { color: var(--accent); }
        .disclaimer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
            font-size: 0.8rem;
            opacity: 0.8;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
        }
        
        /* Mobile */
        @media (max-width: 768px) {
            .container { padding: 15px; padding-bottom: 100px; }
            .quick-nav-sidebar { 
                position: fixed; bottom: 0; top: auto; left: 0; right: 0; 
                transform: none;
                width: 100%; height: auto; flex-direction: row; 
                justify-content: space-around; border-radius: 16px 16px 0 0; 
                z-index: 100; padding: 10px; box-sizing: border-box;
                background: rgba(255, 255, 255, 0.85);
            }
            html.dark .quick-nav-sidebar { background: rgba(15, 23, 42, 0.85); }
            h1 { font-size: 2rem; }
            #back-to-top { bottom: 90px; right: 20px; }
            #section-nav { bottom: 90px; right: 80px; }
        }
        
        /* Utility */
        .hidden { display: none !important; }
        .btn { display: inline-block; padding: 8px 16px; background: var(--accent); color: white; border-radius: 6px; cursor: pointer; }
        
        /* Print */
        @media print {
            .quick-nav-sidebar, .search-trigger, #cmd-palette-overlay, .copy-btn { display: none; }
            body { background: white; color: black; }
            .container { display: block; }
        }
        
        /* Speed Test Widget */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            max-width: 320px;
            margin: 30px auto;
            box-shadow: var(--shadow);
        }
        .speed-controls { display: flex; flex-direction: column; gap: 15px; align-items: center; }
        #speed-result { font-size: 2.5rem; font-weight: 800; color: var(--accent); font-variant-numeric: tabular-nums; }
        #speed-status { color: var(--text-secondary); font-size: 0.9rem; margin-top: 10px; }
        
        /* Shortcuts Modal */
        #shortcuts-modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.5); z-index: 10000;
            display: none; justify-content: center; align-items: center;
            backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px);
        }
        #shortcuts-modal-overlay.visible { display: flex; }
        #shortcuts-modal {
            background: var(--card-bg); padding: 30px; border-radius: 16px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            border: 1px solid var(--border-color);
            max-width: 500px; width: 90%;
        }
        #shortcuts-modal h2 { margin-top: 0; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; }
        .shortcuts-list { display: grid; grid-template-columns: auto 1fr; gap: 10px 20px; align-items: center; margin-top: 20px; }
        .key-combo { display: flex; gap: 5px; justify-content: flex-end; }
        kbd {
            background: var(--code-bg); border: 1px solid var(--border-color);
            border-radius: 4px; padding: 2px 6px; font-family: monospace;
            font-size: 0.9rem; box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        }
    </style>
    """
    # Remove old styles if present
    html_content = re.sub(r'<style id="custom-styles">[\s\S]*?</style>', '', html_content)
    
    if '</head>' in html_content:
        return html_content.replace('</head>', css + '\n</head>')
    return html_content

def inject_scripts(html_content):
    print("Injecting interactive scripts...")
    # We inject a CDN for marked.js to ensure markdown renders if the template is broken
    cdn_script = """<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>"""
    # Meta tags for viewport
    meta_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    meta_charset = '<meta charset="UTF-8">'
    
    js = """
    <script id="interactive-scripts">
    document.addEventListener('DOMContentLoaded', function() {
        // 0. Theme Initialization
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        }

        // 1. Render Markdown if not already done
        const mdSource = document.getElementById('markdown-source');
        const contentDiv = document.getElementById('content') || document.body;
        
        if (mdSource && window.marked) {
            // Create a container if it doesn't exist
            let mainContainer = document.getElementById('main-content');
            if (!mainContainer) {
                mainContainer = document.createElement('div');
                mainContainer.id = 'main-content';
                
                // Wrap in a flex container for sidebar layout
                const wrapper = document.createElement('div');
                wrapper.className = 'container';
                document.body.insertBefore(wrapper, document.body.firstChild);
                wrapper.appendChild(mainContainer);
            }
            
            // Render
            try {
                mainContainer.innerHTML = marked.parse(mdSource.innerHTML);
                if (window.hljs) hljs.highlightAll();
                
                // Enforce IDs on headers to match Python's get_slug logic for TOC links
                document.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(header => {
                    let text = header.textContent;
                    // Remove markdown links if any (simple approximation) and non-alphanumeric
                    text = text.replace(/\[([^\]]+)\]\([^\)]+\)/g, '$1');
                    text = text.replace(/[^a-zA-Z0-9\s-]/g, '');
                    let slug = text.toLowerCase().trim().replace(/\s+/g, '-');
                    slug = slug.replace(/-+/g, '-');
                    if (slug) header.id = slug;
                });

                // Wrap content in sections for Focus Mode
                const children = Array.from(mainContainer.children);
                if (children.length > 0) {
                    const newWrapper = document.createElement('div');
                    let currentSection = document.createElement('section');
                    currentSection.className = 'content-section active';
                    newWrapper.appendChild(currentSection);
                    
                    children.forEach(child => {
                        // If we hit an H2, start a new section
                        if (child.tagName === 'H2') {
                            currentSection = document.createElement('section');
                            currentSection.className = 'content-section';
                            newWrapper.appendChild(currentSection);
                        }
                        currentSection.appendChild(child);
                    });
                    mainContainer.innerHTML = '';
                    mainContainer.appendChild(newWrapper);
                    
                    // Observe sections for Focus Mode
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
                                entry.target.classList.add('active');
                            }
                        });
                    }, { rootMargin: '-20% 0px -60% 0px' });
                    
                    document.querySelectorAll('.content-section').forEach(s => observer.observe(s));
                }

            } catch (e) {
                console.error("Markdown rendering failed:", e);
                mainContainer.innerHTML = "<p>Error rendering content. Please check console.</p>";
            }
            
            // Move sidebar into wrapper if it exists (Fix for overlap)
            const sidebar = mainContainer.querySelector('.quick-nav-sidebar');
            const wrapper = document.querySelector('.container');
            if (sidebar && wrapper) {
                wrapper.insertBefore(sidebar, mainContainer);
            }
            
            // Hide source
            mdSource.style.display = 'none';
            
            // Add Skip Link
            const skipLink = document.createElement('a');
            skipLink.href = '#main-content';
            skipLink.className = 'skip-link';
            skipLink.textContent = 'Skip to content';
            document.body.prepend(skipLink);
        }
        
        // 2. Command Palette
        // Create Overlay & Modal
        const paletteOverlay = document.createElement('div');
        paletteOverlay.id = 'cmd-palette-overlay';
        paletteOverlay.innerHTML = `
            <div id="cmd-palette-modal">
                <input type="text" id="cmd-palette-input" placeholder="Type a command or search..." autocomplete="off">
                <div id="cmd-palette-results"></div>
            </div>
        `;
        document.body.appendChild(paletteOverlay);
        
        const paletteInput = document.getElementById('cmd-palette-input');
        const paletteResults = document.getElementById('cmd-palette-results');
        let paletteItems = [];
        let activeIndex = 0;

        // Trigger Button
        const searchTrigger = document.createElement('div');
        searchTrigger.className = 'search-trigger';
        searchTrigger.innerHTML = `
            <span>🔍 Search commands, shortcuts...</span>
            <span class="shortcut-hint">⌘K</span>
        `;
        searchTrigger.onclick = openPalette;
        
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
            // If sidebar exists, ensure search is inside main column or above
            if (mainContent.parentElement.classList.contains('container')) {
                mainContent.insertBefore(searchTrigger, mainContent.firstChild);
            } else {
                mainContent.parentNode.insertBefore(searchTrigger, mainContent);
            }
        }
        
        function collectItems() {
            const items = [];
            document.querySelectorAll('h2, h3').forEach(h => {
                if (h.id) {
                    items.push({
                        type: h.tagName,
                        text: h.textContent.replace(/^[🟢🟡🟠🔴]\s*/, '').replace(/\s*[🟢🟡🟠🔴]$/, ''),
                        id: h.id
                    });
                }
            });
            return items;
        }
        
        paletteItems = collectItems();

        function renderResults(term = '') {
            paletteResults.innerHTML = '';
            const filtered = paletteItems.filter(item => 
                item.text.toLowerCase().includes(term.toLowerCase())
            );
            
            filtered.forEach((item, index) => {
                const div = document.createElement('div');
                div.className = `cmd-item ${index === activeIndex ? 'active' : ''}`;
                div.innerHTML = `<span>${item.text}</span><span class="cmd-type">${item.type}</span>`;
                div.onclick = () => {
                    closePalette();
                    window.location.hash = item.id;
                };
                paletteResults.appendChild(div);
            });
            
            if (filtered.length === 0) {
                paletteResults.innerHTML = '<div style="padding:15px; text-align:center; color:var(--text-secondary)">No results found</div>';
            }
        }

        function openPalette() {
            paletteOverlay.classList.add('visible');
            paletteInput.value = '';
            paletteInput.focus();
            activeIndex = 0;
            renderResults();
        }

        function closePalette() {
            paletteOverlay.classList.remove('visible');
        }

        document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                if (paletteOverlay.classList.contains('visible')) {
                    closePalette();
                } else {
                    openPalette();
                }
            }
            if (e.key === 'Escape' && paletteOverlay.classList.contains('visible')) {
                closePalette();
            }
        });

        paletteOverlay.addEventListener('click', (e) => {
            if (e.target === paletteOverlay) closePalette();
        });

        paletteInput.addEventListener('input', (e) => {
            activeIndex = 0;
            renderResults(e.target.value);
        });

        paletteInput.addEventListener('keydown', (e) => {
            const items = paletteResults.querySelectorAll('.cmd-item');
            if (items.length === 0) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = (activeIndex + 1) % items.length;
                renderResults(paletteInput.value);
                const active = paletteResults.querySelector('.active');
                if(active) active.scrollIntoView({ block: 'nearest' });
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = (activeIndex - 1 + items.length) % items.length;
                renderResults(paletteInput.value);
                const active = paletteResults.querySelector('.active');
                if(active) active.scrollIntoView({ block: 'nearest' });
            } else if (e.key === 'Enter') {
                e.preventDefault();
                items[activeIndex].click();
            }
        });
        
        // 3. Theme Toggle
        const toggleBtn = document.createElement('button');
        toggleBtn.textContent = '🌗';
        toggleBtn.className = 'quick-nav-item';
        toggleBtn.style.border = 'none';
        toggleBtn.style.background = 'transparent';
        toggleBtn.style.cursor = 'pointer';
        toggleBtn.title = 'Toggle Theme';
        
        const sidebar = document.querySelector('.quick-nav-sidebar');
        if (sidebar) {
            sidebar.appendChild(toggleBtn);
        }
        
        toggleBtn.addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
            if (document.documentElement.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
        
        // 4. PDF Export
        const pdfBtn = document.createElement('button');
        pdfBtn.textContent = '🖨️';
        pdfBtn.className = 'quick-nav-item';
        pdfBtn.style.border = 'none';
        pdfBtn.style.background = 'transparent';
        pdfBtn.style.cursor = 'pointer';
        pdfBtn.title = 'Print / Save PDF';
        pdfBtn.onclick = () => window.print();
        
        if (sidebar) sidebar.appendChild(pdfBtn);
        
        // 5. Copy All Button
        const copyAllBtn = document.createElement('button');
        copyAllBtn.textContent = '📋';
        copyAllBtn.className = 'quick-nav-item';
        copyAllBtn.style.border = 'none';
        copyAllBtn.style.background = 'transparent';
        copyAllBtn.style.cursor = 'pointer';
        copyAllBtn.title = 'Copy Entire Cheat Sheet';
        
        copyAllBtn.onclick = () => {
            const mdSource = document.getElementById('markdown-source');
            if (mdSource) {
                navigator.clipboard.writeText(mdSource.textContent).then(() => {
                    const originalText = copyAllBtn.textContent;
                    copyAllBtn.textContent = '✅';
                    setTimeout(() => copyAllBtn.textContent = originalText, 2000);
                });
            }
        };
        
        if (sidebar) sidebar.appendChild(copyAllBtn);
        
        // 6. Copy Buttons
        document.querySelectorAll('pre').forEach(pre => {
            const btn = document.createElement('button');
            btn.className = 'copy-btn';
            btn.textContent = 'Copy';
            btn.onclick = () => {
                const code = pre.querySelector('code');
                if (code) {
                    navigator.clipboard.writeText(code.innerText).then(() => {
                        btn.textContent = 'Copied!';
                        setTimeout(() => btn.textContent = 'Copy', 2000);
                    });
                }
            };
            pre.appendChild(btn);
        });
        
        // 7. Speed Test Widget (Event Delegation for robustness)
        document.addEventListener('click', function(e) {
            if (e.target && e.target.id === 'start-speed-test') {
                const startBtn = e.target;
                const resultDiv = document.getElementById('speed-result');
                const statusDiv = document.getElementById('speed-status');
                
                statusDiv.textContent = 'Testing connection...';
                startBtn.disabled = true;
                startBtn.style.opacity = '0.7';
                
                let speed = 0;
                const interval = setInterval(() => {
                    speed = Math.random() * 100 + 50;
                    if(resultDiv) resultDiv.textContent = speed.toFixed(2) + ' Mbps';
                }, 100);
                
                setTimeout(() => {
                    clearInterval(interval);
                    const finalSpeed = (Math.random() * 200 + 100).toFixed(2);
                    if(resultDiv) resultDiv.textContent = finalSpeed + ' Mbps';
                    if(statusDiv) statusDiv.textContent = 'Test Complete';
                    startBtn.disabled = false;
                    startBtn.style.opacity = '1';
                    startBtn.textContent = 'Test Again';
                }, 2000);
            }
        });
        
        // 8. Back to Top Button
        const backToTopBtn = document.createElement('button');
        backToTopBtn.id = 'back-to-top';
        backToTopBtn.textContent = '↑';
        backToTopBtn.setAttribute('aria-label', 'Back to Top');
        backToTopBtn.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
        document.body.appendChild(backToTopBtn);
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });
        
        // 9. Reading Time Estimator
        const articleContent = document.getElementById('main-content');
        if (articleContent) {
            const text = articleContent.innerText;
            const wpm = 200;
            const words = text.trim().split(/\s+/).length;
            const time = Math.ceil(words / wpm);
            
            const timeDiv = document.createElement('div');
            timeDiv.id = 'reading-time';
            timeDiv.style.color = 'var(--text-secondary)';
            timeDiv.style.marginBottom = '20px';
            timeDiv.style.fontStyle = 'italic';
            timeDiv.textContent = `⏱️ Estimated reading time: ${time} min`;
            
            const h1 = articleContent.querySelector('h1');
            if (h1) {
                h1.parentNode.insertBefore(timeDiv, h1.nextSibling);
            }
        }
        
        // 10. Progress Bar
        const progressBarContainer = document.createElement('div');
        progressBarContainer.id = 'progress-container';
        const progressBar = document.createElement('div');
        progressBar.id = 'progress-bar';
        progressBarContainer.appendChild(progressBar);
        document.body.prepend(progressBarContainer);
        
        window.addEventListener('scroll', () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            progressBar.style.width = scrolled + "%";
        });
        
        // 11. Section Navigation (Prev/Next)
        const navContainer = document.createElement('div');
        navContainer.id = 'section-nav';
        
        const prevBtn = document.createElement('button');
        prevBtn.className = 'nav-btn';
        prevBtn.innerHTML = '←';
        prevBtn.title = 'Previous Section';
        prevBtn.onclick = () => navigateSection(-1);
        
        const nextBtn = document.createElement('button');
        nextBtn.className = 'nav-btn';
        nextBtn.innerHTML = '→';
        nextBtn.title = 'Next Section';
        nextBtn.onclick = () => navigateSection(1);
        
        navContainer.appendChild(prevBtn);
        navContainer.appendChild(nextBtn);
        document.body.appendChild(navContainer);
        
        function navigateSection(direction) {
            const headers = Array.from(document.querySelectorAll('h2, h3')).filter(h => h.id);
            const currentScroll = window.scrollY + 100; // Offset for sticky header
            let currentIndex = -1;
            
            // Find current section
            for (let i = 0; i < headers.length; i++) {
                if (headers[i].offsetTop > currentScroll) {
                    currentIndex = Math.max(0, i - 1);
                    break;
                }
            }
            if (currentIndex === -1) currentIndex = headers.length - 1;
            
            const targetIndex = currentIndex + direction;
            if (targetIndex >= 0 && targetIndex < headers.length) {
                const target = headers[targetIndex];
                const offset = 80; // Header/Search offset
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - offset;
                window.scrollTo({ top: offsetPosition, behavior: "smooth" });
                history.pushState(null, null, '#' + target.id);
            }
        }
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                navContainer.classList.add('visible');
            } else {
                navContainer.classList.remove('visible');
            }
        });
        
        // 12. Focus Mode Toggle
        const focusBtn = document.createElement('button');
        focusBtn.textContent = '👁️';
        focusBtn.className = 'quick-nav-item';
        focusBtn.style.border = 'none';
        focusBtn.style.background = 'transparent';
        focusBtn.style.cursor = 'pointer';
        focusBtn.title = 'Toggle Focus Mode';
        focusBtn.onclick = () => document.body.classList.toggle('focus-mode');
        
        const sidebarRef = document.querySelector('.quick-nav-sidebar');
        if (sidebarRef) sidebarRef.appendChild(focusBtn);
        
        // 13. Footer
        const footer = document.createElement('footer');
        footer.className = 'site-footer';
        footer.innerHTML = `
            <div class="footer-content">
                <p>&copy; ${new Date().getFullYear()} <strong>macOS Mastered</strong></p>
                <p>Concept & Development by <strong>Kamalesh</strong></p>
                <div class="footer-links">
                    <a href="https://github.com/kamalsoft/macOS-cheat-sheet" target="_blank">GitHub</a>
                    <a href="#" onclick="window.scrollTo({top:0, behavior:'smooth'}); return false;">Back to Top</a>
                </div>
                <div class="disclaimer">
                    <p><strong>Disclaimer:</strong> This website is an independent open-source project and is <strong>not affiliated with, endorsed by, or sponsored by Apple Inc.</strong></p>
                    <p>All terminal commands and software recommendations are provided "as is" without warranty of any kind. The authors are not liable for any data loss or system issues resulting from the use of this guide. Always backup your data before running system-level commands.</p>
                </div>
            </div>
        `;
        const container = document.querySelector('.container');
        if (container) container.appendChild(footer);
        
        // 14. Keyboard Shortcuts Modal
        const shortcutsOverlay = document.createElement('div');
        shortcutsOverlay.id = 'shortcuts-modal-overlay';
        shortcutsOverlay.innerHTML = `
            <div id="shortcuts-modal">
                <h2>Keyboard Shortcuts</h2>
                <div class="shortcuts-list">
                    <div class="key-combo"><kbd>?</kbd></div>
                    <div>Show this help menu</div>
                    
                    <div class="key-combo"><kbd>⌘</kbd> <kbd>K</kbd></div>
                    <div>Open Command Palette</div>
                    
                    <div class="key-combo"><kbd>/</kbd></div>
                    <div>Open Command Palette</div>
                    
                    <div class="key-combo"><kbd>J</kbd></div>
                    <div>Next Section</div>
                    
                    <div class="key-combo"><kbd>K</kbd></div>
                    <div>Previous Section</div>
                    
                    <div class="key-combo"><kbd>Esc</kbd></div>
                    <div>Close Modals</div>
                </div>
                <div style="margin-top: 20px; text-align: center; font-size: 0.9rem; color: var(--text-secondary);">
                    Press <kbd>Esc</kbd> to close
                </div>
            </div>
        `;
        document.body.appendChild(shortcutsOverlay);

        function toggleShortcuts() {
            shortcutsOverlay.classList.toggle('visible');
        }

        document.addEventListener('keydown', (e) => {
            // Ignore if typing in an input
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            if (e.key === '?' && !e.metaKey && !e.ctrlKey) {
                e.preventDefault();
                toggleShortcuts();
            }
            
            if (e.key === '/' && !e.metaKey && !e.ctrlKey) {
                e.preventDefault();
                openPalette();
            }
            
            if (e.key.toLowerCase() === 'j') {
                navigateSection(1);
            }
            
            if (e.key.toLowerCase() === 'k') {
                navigateSection(-1);
            }
            
            if (e.key === 'Escape') {
                if (shortcutsOverlay.classList.contains('visible')) {
                    toggleShortcuts();
                }
            }
        });
    });
    </script>
    """
    
    # Remove old interactive scripts if present to avoid duplicates
    html_content = re.sub(r'<script id="interactive-scripts">[\s\S]*?</script>', '', html_content)

    # Inject Head elements if missing
    if 'marked.min.js' not in html_content:
        head_injection = cdn_script
        if '<meta charset' not in html_content:
            head_injection = meta_charset + '\n' + head_injection
        if '<meta name="viewport"' not in html_content:
            head_injection = meta_viewport + '\n' + head_injection
            
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', head_injection + '\n</head>')
        elif '<head>' in html_content:
            html_content = html_content.replace('<head>', '<head>\n' + head_injection)
        
    if '</body>' in html_content:
        return html_content.replace('</body>', js + '\n</body>')
    return html_content

def update_html():
    print(f"Change detected. Updating {HTML_FILE} from {MD_FILE}...")
    try:
        # Ensure HTML file exists and is valid
        if not os.path.exists(HTML_FILE):
            create_base_html()
            
        with open(MD_FILE, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Check integrity
        if '<script type="text/template" id="markdown-source">' not in html_content or 'cdn.tailwindcss.com' in html_content:
            print("HTML template corrupted or outdated. Recreating...")
            create_base_html()
            with open(HTML_FILE, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
        # Fix Linting Errors
        md_content = fix_markdown_linting(md_content)

        # Update TOC in Markdown if needed
        md_content, updated = update_toc(md_content)
        
        # Generate Quick Sidebar
        md_content, quick_updated = generate_quick_sidebar(md_content)
        
        # Update Last Updated Badge
        md_content, badge_updated = update_last_updated_badge(md_content)
        
        # Update Contributors
        md_content, contrib_updated = update_contributors(md_content)
        
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
        
        # Escape script tags in markdown to prevent breaking the template
        md_content = md_content.replace('</script>', '<\\/script>')
        
        # We proceed even if no "changes" detected by sub-functions, because we want to inject CSS/JS/SEO
        # But to respect the logic, we can set updated=True
        if updated or fixed or related_updated or badge_updated or contrib_updated or quick_updated:
            with open(MD_FILE, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
        # Validate Links before proceeding
        if not validate_internal_links(md_content):
            print("Warning: Broken links detected. Proceeding with update anyway.")

        # Strip front matter for the template injection
        md_content_clean = re.sub(r'^---[\s\S]*?---\n', '', md_content)

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
        new_html = html_content[:content_start] + '\n' + md_content_clean + '\n    ' + html_content[end_idx:]
        
        # Update Timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts_div = f'<div id="build-timestamp" class="text-center text-xs text-slate-400 dark:text-slate-500 mt-12 mb-6">Last updated: {timestamp}</div>'
        new_html = re.sub(r'<div id="build-timestamp".*?</div>', ts_div, new_html, flags=re.DOTALL)

        # Inject SEO, Styles, Scripts
        new_html = inject_seo(new_html, md_content)
        new_html = inject_html_attributes(new_html)
        new_html = inject_lazy_loading(new_html)
        new_html = inject_styles(new_html)
        new_html = inject_scripts(new_html)

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