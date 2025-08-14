#!/usr/bin/env python3
"""
CSV Parser for Awesome ChatGPT Prompts
Processes the CSV and creates categorized prompt files
"""

import csv
import urllib.request
import os
import re

def fetch_csv_data():
    """Fetch the CSV data from GitHub"""
    url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/refs/heads/main/prompts.csv"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    return data

def parse_csv_data(csv_data):
    """Parse CSV data and return list of prompts"""
    prompts = []
    lines = csv_data.strip().split('\n')
    reader = csv.reader(lines)
    
    # Skip header if present
    header = next(reader, None)
    print(f"Header: {header}")
    
    for row in reader:
        if len(row) >= 2:
            act = row[0].strip()
            prompt = row[1].strip()
            prompts.append({
                'act': act,
                'prompt': prompt
            })
    
    return prompts

def categorize_prompt(act):
    """Categorize prompts based on their role/act"""
    act_lower = act.lower()
    
    # Technical & Development
    if any(word in act_lower for word in ['developer', 'programmer', 'coder', 'software', 'terminal', 'console', 'javascript', 'python', 'web', 'tech', 'engineer', 'database', 'sql', 'regex', 'git', 'stackoverflow']):
        return 'Technical'
    
    # Writing & Content
    elif any(word in act_lower for word in ['writer', 'poet', 'novelist', 'journalist', 'author', 'editor', 'copywriter', 'storyteller', 'screenwriter', 'blogger', 'content']):
        return 'Writing'
    
    # Education & Learning
    elif any(word in act_lower for word in ['teacher', 'instructor', 'tutor', 'professor', 'educator', 'academy', 'student', 'learning', 'math', 'science', 'history', 'language', 'translator']):
        return 'Education'
    
    # Business & Professional
    elif any(word in act_lower for word in ['manager', 'consultant', 'advisor', 'business', 'financial', 'accountant', 'salesperson', 'recruiter', 'interviewer', 'ceo', 'entrepreneur', 'marketing']):
        return 'Business'
    
    # Creative & Entertainment
    elif any(word in act_lower for word in ['artist', 'musician', 'composer', 'actor', 'comedian', 'magician', 'designer', 'creative', 'entertainment', 'game', 'film']):
        return 'Creative'
    
    # Health & Wellness
    elif any(word in act_lower for word in ['doctor', 'therapist', 'psychologist', 'dentist', 'nurse', 'fitness', 'yoga', 'mental health', 'medical']):
        return 'Health'
    
    # Role-Playing & Characters
    elif any(word in act_lower for word in ['character', 'person', 'friend', 'assistant', 'guide', 'companion', 'simulator']):
        return 'Role-Playing'
    
    # Analysis & Research
    elif any(word in act_lower for word in ['analyst', 'researcher', 'critic', 'reviewer', 'commentator', 'expert', 'specialist']):
        return 'Analysis'
    
    else:
        return 'Miscellaneous'

def sanitize_filename(name):
    """Create a safe filename from the act name"""
    # Remove special characters and replace spaces with hyphens
    filename = re.sub(r'[^\w\s-]', '', name)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def create_prompt_file(prompt_data, category, base_path):
    """Create individual prompt file using template format"""
    act = prompt_data['act']
    prompt_text = prompt_data['prompt']
    
    filename = f"{category} - {sanitize_filename(act)}.md"
    filepath = os.path.join(base_path, filename)
    
    # Estimate typical length based on prompt complexity
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
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename
    except Exception as e:
        print(f"Error creating file {filename}: {e}")
        return None

if __name__ == "__main__":
    # Test the functions
    print("Fetching CSV data...")
    csv_data = fetch_csv_data()
    
    print("Parsing prompts...")
    prompts = parse_csv_data(csv_data)
    
    print(f"Found {len(prompts)} prompts")
    
    # Show first few for testing
    for i, prompt in enumerate(prompts[:5]):
        print(f"{i+1}. {prompt['act']}")
        category = categorize_prompt(prompt['act'])
        print(f"   Category: {category}")
        print(f"   Prompt length: {len(prompt['prompt'])} characters")
        print()