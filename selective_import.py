#!/usr/bin/env python3
"""
Selective import of high-value prompts from Awesome ChatGPT Prompts
Focuses on the most practical and useful prompts for professional work
"""

import csv
import urllib.request
import os
import re

def fetch_prompts():
    """Fetch and parse all prompts"""
    url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/refs/heads/main/prompts.csv"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    
    prompts = []
    lines = data.strip().split('\n')
    reader = csv.reader(lines)
    next(reader, None)  # Skip header
    
    for row in reader:
        if len(row) >= 2:
            prompts.append({'act': row[0].strip(), 'prompt': row[1].strip()})
    
    return prompts

def select_high_value_prompts(prompts):
    """Select the most valuable prompts for professional use"""
    high_value_keywords = [
        # Technical
        'senior frontend developer', 'fullstack software developer', 'software quality assurance tester',
        'regex generator', 'cyber security specialist', 'web design consultant', 'it architect',
        'machine learning engineer', 'data scientist', 'database administrator',
        
        # Business & Professional  
        'product manager', 'startup idea generator', 'business analyst', 'investment manager',
        'marketing expert', 'sales manager', 'career counselor', 'recruiter',
        
        # Writing & Content
        'technical writer', 'content creator', 'copywriter', 'proofreader', 'journalist',
        'essay writer', 'academic', 'researcher',
        
        # Analysis & Research
        'data analyst', 'market research analyst', 'financial analyst', 'statistician',
        'scientific data visualizer', 'expert', 'consultant',
        
        # Education & Learning
        'language teacher', 'learning coach', 'instructor', 'translator', 'mentor',
        
        # Creative (Professional)
        'ux/ui developer', 'interior decorator', 'artist', 'designer'
    ]
    
    selected = []
    for prompt in prompts:
        act_lower = prompt['act'].lower()
        if any(keyword in act_lower for keyword in high_value_keywords):
            selected.append(prompt)
    
    return selected

def categorize_prompt(act):
    """Categorize prompts"""
    act_lower = act.lower()
    
    if any(word in act_lower for word in ['developer', 'engineer', 'programmer', 'technical', 'software', 'cyber', 'data scientist', 'machine learning', 'database', 'architect', 'regex', 'qa']):
        return 'Technical'
    elif any(word in act_lower for word in ['writer', 'content', 'copywriter', 'journalist', 'proofreader', 'academic', 'essay']):
        return 'Writing'
    elif any(word in act_lower for word in ['teacher', 'instructor', 'mentor', 'translator', 'learning', 'coach']):
        return 'Education'
    elif any(word in act_lower for word in ['manager', 'analyst', 'business', 'consultant', 'investment', 'marketing', 'sales', 'recruiter', 'startup', 'career']):
        return 'Business'
    elif any(word in act_lower for word in ['designer', 'artist', 'ux/ui', 'decorator']):
        return 'Creative'
    elif any(word in act_lower for word in ['researcher', 'statistician', 'expert', 'visualizer']):
        return 'Analysis'
    else:
        return 'Professional'

def sanitize_filename(name):
    """Create safe filename"""
    filename = re.sub(r'[^\w\s-]', '', name)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def create_prompt_files(selected_prompts):
    """Create prompt files for selected prompts"""
    created_files = {}
    
    for prompt in selected_prompts:
        category = categorize_prompt(prompt['act'])
        act = prompt['act']
        prompt_text = prompt['prompt']
        
        filename = f"{category} - {sanitize_filename(act)}.md"
        
        content = f"""# {category} - {act}

## Prompt
```
{prompt_text}
```

## Context
- **Best for**: Professional {category.lower()} tasks requiring domain expertise
- **Avoid when**: Need factual information outside the role's expertise
- **Typical length**: 200-800 words depending on complexity

## Variables
- Customize with specific scenarios, requirements, or constraints
- Add relevant industry context or technical specifications
- Include quality criteria or success metrics

## Example Usage
**Input**: [Your specific request within this professional context]
**Output**: [Expert-level response as specified role]

## Effectiveness
Rating: ⭐⭐⭐ (to be tested)
Last updated: 2025-07-27

## Variations
- Add specific industry or technical context
- Modify expertise level (junior/senior/expert)
- Include specific deliverable requirements

## Source
From: [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
"""
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if category not in created_files:
                created_files[category] = []
            created_files[category].append((filename, act))
            
            print(f"✓ Created: {filename}")
        except Exception as e:
            print(f"✗ Error creating {filename}: {e}")
    
    return created_files

def main():
    print("Fetching all prompts...")
    all_prompts = fetch_prompts()
    print(f"Total prompts available: {len(all_prompts)}")
    
    print("\nSelecting high-value professional prompts...")
    selected = select_high_value_prompts(all_prompts)
    print(f"Selected {len(selected)} high-value prompts")
    
    print("\nCreating prompt files...")
    created_files = create_prompt_files(selected)
    
    print(f"\nSummary:")
    total_created = sum(len(files) for files in created_files.values())
    print(f"Created {total_created} professional prompt files")
    
    for category, files in created_files.items():
        print(f"  {category}: {len(files)} prompts")
    
    return created_files

if __name__ == "__main__":
    created_files = main()