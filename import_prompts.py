#!/usr/bin/env python3
"""
Import Awesome ChatGPT Prompts into Obsidian vault
Creates categorized prompt files and updates the main index
"""

import csv
import urllib.request
import os
import re
from collections import defaultdict

def fetch_and_parse_prompts():
    """Fetch CSV data and parse prompts"""
    url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/refs/heads/main/prompts.csv"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    
    prompts = []
    lines = data.strip().split('\n')
    reader = csv.reader(lines)
    
    # Skip header
    next(reader, None)
    
    for row in reader:
        if len(row) >= 2:
            act = row[0].strip()
            prompt = row[1].strip()
            prompts.append({'act': act, 'prompt': prompt})
    
    return prompts

def categorize_prompt(act):
    """Categorize prompts based on their role/act"""
    act_lower = act.lower()
    
    # Technical & Development
    if any(word in act_lower for word in ['developer', 'programmer', 'coder', 'software', 'terminal', 'console', 'javascript', 'python', 'web', 'tech', 'engineer', 'database', 'sql', 'regex', 'git', 'stackoverflow', 'solr', 'senior frontend', 'fullstack', 'cyber security', 'it architect', 'ux/ui', 'machine learning']):
        return 'Technical'
    
    # Writing & Content
    elif any(word in act_lower for word in ['writer', 'poet', 'novelist', 'journalist', 'author', 'editor', 'copywriter', 'storyteller', 'screenwriter', 'blogger', 'content', 'essay writer', 'plagiarism checker', 'proofreader']):
        return 'Writing'
    
    # Education & Learning
    elif any(word in act_lower for word in ['teacher', 'instructor', 'tutor', 'professor', 'educator', 'academy', 'student', 'learning', 'math', 'science', 'history', 'language', 'translator', 'etymologist', 'pronunciation assistant']):
        return 'Education'
    
    # Business & Professional
    elif any(word in act_lower for word in ['manager', 'consultant', 'advisor', 'business', 'financial', 'accountant', 'salesperson', 'recruiter', 'interviewer', 'ceo', 'entrepreneur', 'marketing', 'investment', 'real estate', 'career counselor']):
        return 'Business'
    
    # Creative & Entertainment
    elif any(word in act_lower for word in ['artist', 'musician', 'composer', 'actor', 'comedian', 'magician', 'designer', 'creative', 'entertainment', 'game', 'film', 'ascii artist', 'makeup artist', 'interior decorator']):
        return 'Creative'
    
    # Health & Wellness
    elif any(word in act_lower for word in ['doctor', 'therapist', 'psychologist', 'dentist', 'nurse', 'fitness', 'yoga', 'mental health', 'medical', 'personal trainer', 'life coach']):
        return 'Health'
    
    # Role-Playing & Characters
    elif any(word in act_lower for word in ['character', 'person', 'friend', 'assistant', 'guide', 'companion', 'simulator', 'lunatic', 'drunk person', 'relationship coach', 'motivational coach']):
        return 'Role-Playing'
    
    # Analysis & Research
    elif any(word in act_lower for word in ['analyst', 'researcher', 'critic', 'reviewer', 'commentator', 'expert', 'specialist', 'statistician', 'scientific data visualizer']):
        return 'Analysis'
    
    else:
        return 'Miscellaneous'

def sanitize_filename(name):
    """Create a safe filename from the act name"""
    filename = re.sub(r'[^\w\s-]', '', name)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def create_prompt_file(prompt_data, category):
    """Create individual prompt file"""
    act = prompt_data['act']
    prompt_text = prompt_data['prompt']
    
    filename = f"{category} - {sanitize_filename(act)}.md"
    
    # Estimate typical length
    word_count = len(prompt_text.split())
    if word_count < 50:
        typical_length = "50-200 words"
    elif word_count < 100:
        typical_length = "200-500 words"
    else:
        typical_length = "500+ words"
    
    content = f"""# {category} - {act}

## Prompt
```
{prompt_text}
```

## Context
- **Best for**: Role-playing scenarios, specific domain expertise
- **Avoid when**: Need factual information outside the role's expertise
- **Typical length**: {typical_length}

## Variables
- Customize the prompt with specific scenarios or requirements
- Add context about your specific use case
- Include any constraints or preferences

## Example Usage
**Input**: [Your specific request within this role context]
**Output**: [Response in character/role as specified]

## Effectiveness
Rating: ⭐⭐⭐ (to be tested)
Last updated: 2025-07-27

## Variations
- Add specific industry context
- Modify tone (formal/casual/expert level)
- Include specific constraints or requirements

## Source
From: [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
"""
    
    return filename, content

def main():
    print("Fetching prompts...")
    prompts = fetch_and_parse_prompts()
    print(f"Found {len(prompts)} prompts")
    
    # Categorize prompts
    categories = defaultdict(list)
    for prompt in prompts:
        category = categorize_prompt(prompt['act'])
        categories[category].append(prompt)
    
    print("\nCategories found:")
    for category, prompt_list in categories.items():
        print(f"  {category}: {len(prompt_list)} prompts")
    
    # Create files for first 20 prompts as a sample
    print(f"\nCreating sample files (first 20 prompts)...")
    created_files = []
    
    for i, prompt in enumerate(prompts[:20]):
        category = categorize_prompt(prompt['act'])
        filename, content = create_prompt_file(prompt, category)
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            created_files.append((category, filename, prompt['act']))
            print(f"✓ Created: {filename}")
        except Exception as e:
            print(f"✗ Error creating {filename}: {e}")
    
    print(f"\nCreated {len(created_files)} prompt files")
    
    # Return summary for updating the main index
    return categories, created_files

if __name__ == "__main__":
    categories, created_files = main()