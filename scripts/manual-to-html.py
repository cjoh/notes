#!/usr/bin/env python3
"""
Core Values Recovery - Coaching Manual HTML Generator
Converts markdown coaching manuals to branded, printable HTML

Usage: python manual-to-html.py path/to/manual.md
"""

import sys
import os
import re
from pathlib import Path
import argparse
from datetime import datetime

def get_brand_colors():
    """Core Values Recovery brand colors"""
    return {
        'primary': '#1d4486',
        'white': '#ffffff',
        'light_gray': '#f8f9fa',
        'medium_gray': '#6c757d',
        'dark_gray': '#343a40',
        'accent': '#e3f2fd'
    }

def get_css_styles():
    """Generate CSS with CVR branding"""
    colors = get_brand_colors()
    
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue:wght@400&family=Open+Sans:wght@400;600;700&display=swap');
    
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    body {{
        font-family: 'Open Sans', Arial, sans-serif;
        line-height: 1.6;
        color: {colors['dark_gray']};
        background: {colors['white']};
        font-size: 12px;
    }}
    
    .container {{
        max-width: 8.5in;
        margin: 0 auto;
        padding: 0.75in;
        background: {colors['white']};
    }}
    
    /* Header */
    .header {{
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 3px solid {colors['primary']};
    }}
    
    .logo {{
        max-width: 200px;
        height: auto;
        margin-bottom: 1rem;
    }}
    
    .company-name {{
        font-family: 'Bebas Neue', sans-serif;
        font-weight: 400;
        font-size: 24px;
        color: {colors['primary']};
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }}
    
    .tagline {{
        font-size: 10px;
        color: {colors['medium_gray']};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    /* Main Title */
    h1 {{
        font-family: 'Bebas Neue', sans-serif;
        font-weight: 400;
        font-size: 32px;
        color: {colors['primary']};
        text-align: center;
        margin: 2rem 0 1.5rem 0;
        line-height: 1.2;
        letter-spacing: 1px;
    }}
    
    /* Section Headers */
    h2 {{
        font-family: 'Bebas Neue', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: {colors['primary']};
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid {colors['accent']};
        letter-spacing: 0.5px;
    }}
    
    h3 {{
        font-family: 'Bebas Neue', sans-serif;
        font-weight: 400;
        font-size: 16px;
        color: {colors['primary']};
        margin: 1.5rem 0 0.75rem 0;
        letter-spacing: 0.5px;
    }}
    
    h4 {{
        font-weight: 600;
        color: {colors['primary']};
        margin: 1rem 0 0.5rem 0;
        font-size: 13px;
    }}
    
    /* Paragraphs and Text */
    p {{
        margin: 0.75rem 0;
        text-align: justify;
        hyphens: auto;
    }}
    
    em {{
        font-style: italic;
        color: {colors['medium_gray']};
        font-size: 11px;
    }}
    
    strong {{
        font-weight: 700;
        color: {colors['primary']};
    }}
    
    /* Lists */
    ul, ol {{
        margin: 0.75rem 0 0.75rem 1.5rem;
    }}
    
    li {{
        margin: 0.25rem 0;
        line-height: 1.5;
    }}
    
    /* Horizontal Rules */
    hr {{
        border: none;
        height: 2px;
        background: linear-gradient(to right, {colors['primary']}, {colors['accent']}, {colors['primary']});
        margin: 2rem 0;
    }}
    
    /* Quotes and Highlights */
    blockquote {{
        background: {colors['light_gray']};
        border-left: 4px solid {colors['primary']};
        padding: 1rem 1.5rem;
        margin: 1rem 0;
        font-style: italic;
    }}
    
    /* Code and Technical Text */
    code {{
        background: {colors['light_gray']};
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 11px;
    }}
    
    pre {{
        background: {colors['light_gray']};
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid {colors['primary']};
        margin: 1rem 0;
        overflow-x: auto;
    }}
    
    /* Callout Boxes */
    .callout {{
        background: {colors['accent']};
        border: 1px solid {colors['primary']};
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }}
    
    .callout h4 {{
        margin-top: 0;
        color: {colors['primary']};
    }}
    
    /* Time Blocks */
    .time-block {{
        background: {colors['white']};
        border: 2px solid {colors['primary']};
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        page-break-inside: avoid;
    }}
    
    .time-block h3 {{
        margin-top: 0;
        background: {colors['primary']};
        color: {colors['white']};
        padding: 0.5rem 1rem;
        margin: -1rem -1rem 1rem -1rem;
        border-radius: 3px 3px 0 0;
    }}
    
    /* Footer */
    .footer {{
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 2px solid {colors['primary']};
        text-align: center;
        font-size: 10px;
        color: {colors['medium_gray']};
    }}
    
    /* Print Styles */
    @media print {{
        body {{
            font-size: 11px;
        }}
        
        .container {{
            padding: 0.5in;
        }}
        
        h1 {{
            font-size: 28px;
        }}
        
        h2 {{
            font-size: 18px;
        }}
        
        .time-block, .callout {{
            page-break-inside: avoid;
        }}
        
        .header {{
            page-break-after: avoid;
        }}
    }}
    
    /* Table Styles */
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
    }}
    
    th, td {{
        border: 1px solid {colors['medium_gray']};
        padding: 0.5rem;
        text-align: left;
    }}
    
    th {{
        background: {colors['primary']};
        color: {colors['white']};
        font-weight: 600;
    }}
    
    tr:nth-child(even) {{
        background: {colors['light_gray']};
    }}
    </style>
    """

def markdown_to_html(content):
    """Convert markdown content to HTML with custom enhancements"""
    
    # Convert headers - check for time blocks first
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    
    # Special handling for time block headers (contains time range and em dash)
    content = re.sub(r'^### (\d+[–—-]\d+\s+min\s+[–—-]\s+.+)$', r'<h3 class="time-header">\1</h3>', content, flags=re.MULTILINE)
    
    # Regular h3 headers (not time blocks)
    content = re.sub(r'^### ((?!\d+[–—-]\d+\s+min).+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    
    content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', content, flags=re.MULTILINE)
    
    # Convert horizontal rules
    content = re.sub(r'^---+$', '<hr>', content, flags=re.MULTILINE)
    
    # Convert emphasis and strong
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    
    # Convert lists (handles blank lines within lists)
    lines = content.split('\n')
    in_list = False
    list_type = None  # 'ul' or 'ol'
    result_lines = []
    
    for i, line in enumerate(lines):
        if re.match(r'^- ', line):
            # Bullet list
            if not in_list or list_type != 'ul':
                if in_list:
                    result_lines.append(f'</{list_type}>')
                result_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            result_lines.append(f'<li>{line[2:]}</li>')
        elif re.match(r'^\d+\. ', line):
            # Numbered list
            if not in_list or list_type != 'ol':
                if in_list:
                    result_lines.append(f'</{list_type}>')
                result_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            result_lines.append(f'<li>{re.sub(r"^\d+\. ", "", line)}</li>')
        elif line.strip() == '' and in_list:
            # Blank line within a list - check if next non-blank line continues the list
            next_line_idx = i + 1
            while next_line_idx < len(lines) and lines[next_line_idx].strip() == '':
                next_line_idx += 1
            
            if next_line_idx < len(lines):
                next_line = lines[next_line_idx]
                # If next line continues the same list type, skip the blank line
                if ((list_type == 'ul' and re.match(r'^- ', next_line)) or 
                    (list_type == 'ol' and re.match(r'^\d+\. ', next_line))):
                    continue  # Skip blank line
            
            # Otherwise, close the list and add the blank line
            if in_list:
                result_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            result_lines.append(line)
        else:
            if in_list and line.strip() != '':
                result_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            result_lines.append(line)
    
    if in_list:
        result_lines.append(f'</{list_type}>')
    
    content = '\n'.join(result_lines)
    
    # Convert paragraphs
    paragraphs = content.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            # Check if it's a single line that's not HTML
            if '\n' not in para:
                html_paragraphs.append(f'<p>{para}</p>')
            else:
                # Multi-line paragraph
                lines = para.split('\n')
                if all(not line.startswith('<') for line in lines if line.strip()):
                    html_paragraphs.append(f'<p>{" ".join(lines)}</p>')
                else:
                    html_paragraphs.append(para)
        else:
            html_paragraphs.append(para)
    
    return '\n\n'.join(html_paragraphs)

def create_header():
    """Create the branded header"""
    return """
    <div class="header">
        <div class="company-name">CORE VALUES RECOVERY</div>
        <div class="tagline">Professional Coaching &amp; Development</div>
    </div>
    """

def create_footer():
    """Create the branded footer"""
    current_year = datetime.now().year
    return f"""
    <div class="footer">
        <p>&copy; {current_year} Core Values Recovery. All rights reserved.</p>
        <p>Professional coaching materials for internal use only.</p>
    </div>
    """

def generate_html(markdown_file, output_file=None):
    """Generate branded HTML from markdown file"""
    
    # Read the markdown file
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{markdown_file}' not found.")
        return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Extract title from first line or filename
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(markdown_file).stem.replace('-', ' ').title()
    
    # Convert markdown to HTML
    html_content = markdown_to_html(content)
    
    # Generate output filename if not provided
    if output_file is None:
        output_file = Path(markdown_file).with_suffix('.html')
    
    # Create complete HTML document
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Core Values Recovery</title>
    {get_css_styles()}
</head>
<body>
    <div class="container">
        {create_header()}
        {html_content}
        {create_footer()}
    </div>
</body>
</html>"""
    
    # Write the HTML file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_document)
        print(f"✅ Generated: {output_file}")
        return True
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return False

def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(
        description="Convert Core Values Recovery coaching manuals to branded HTML"
    )
    parser.add_argument(
        'markdown_file', 
        help='Path to the markdown file to convert'
    )
    parser.add_argument(
        '-o', '--output', 
        help='Output HTML file path (default: same name with .html extension)'
    )
    parser.add_argument(
        '--preview', 
        action='store_true',
        help='Open the generated HTML file in default browser'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.markdown_file):
        print(f"Error: File '{args.markdown_file}' does not exist.")
        return 1
    
    success = generate_html(args.markdown_file, args.output)
    
    if success and args.preview:
        import webbrowser
        output_path = args.output or Path(args.markdown_file).with_suffix('.html')
        webbrowser.open(f'file://{os.path.abspath(output_path)}')
        print(f"🌐 Opening {output_path} in browser...")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())