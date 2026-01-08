import time
import os
import sys
import re
import datetime

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
        # Clean title: remove markdown links and special chars to match likely ID
        clean_title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', title)
        clean_title = re.sub(r'[^\w\s-]', '', clean_title)
        slug = clean_title.lower().strip().replace(' ', '-')
        slug = re.sub(r'-+', '-', slug)
        
        if slug:
            sitemap.append(f'  <url>\n    <loc>{base_url}#{slug}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.5</priority>\n  </url>')
            
    sitemap.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap))

def update_html():
    print(f"Change detected. Updating {HTML_FILE} from {MD_FILE}...")
    try:
        with open(MD_FILE, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
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