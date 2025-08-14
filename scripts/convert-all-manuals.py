#!/usr/bin/env python3
"""
Convert all coaching manuals to branded HTML for PDF generation
"""

import os
import glob
from pathlib import Path
import subprocess

def find_coaching_manuals():
    """Find all coaching manual markdown files"""
    patterns = [
        '**/*manual*.md',
        '**/*coaching*.md',
        '**/*guide*.md'
    ]
    
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern, recursive=True))
    
    # Filter out any files that might not be coaching manuals
    coaching_files = []
    for file in files:
        # Check if it's likely a coaching manual based on content or location
        if any(keyword in file.lower() for keyword in ['manual', 'coach', 'guide', 'curriculum']):
            coaching_files.append(file)
    
    return list(set(coaching_files))  # Remove duplicates

def convert_manual(manual_file):
    """Convert a single manual to HTML"""
    try:
        result = subprocess.run([
            'python', 
            'scripts/manual-to-html.py', 
            manual_file
        ], capture_output=True, text=True, check=True)
        
        print(f"✅ Converted: {manual_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to convert {manual_file}: {e}")
        return False

def main():
    """Main function"""
    print("🔍 Finding coaching manuals...")
    manuals = find_coaching_manuals()
    
    if not manuals:
        print("No coaching manuals found.")
        return
    
    print(f"📚 Found {len(manuals)} manual(s):")
    for manual in manuals:
        print(f"  - {manual}")
    
    print("\n🔄 Converting to HTML...")
    success_count = 0
    
    for manual in manuals:
        if convert_manual(manual):
            success_count += 1
    
    print(f"\n✨ Conversion complete! {success_count}/{len(manuals)} files converted successfully.")
    print("\n📄 To convert HTML to PDF:")
    print("1. Open the HTML files in your browser")
    print("2. Use Print > Save as PDF")
    print("3. Or use a tool like wkhtmltopdf for batch conversion")

if __name__ == "__main__":
    main()