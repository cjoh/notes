# Utility - Text Cleaning

## Prompt

You are an expert at cleaning up broken and malformatted text, such as strange line breaks, formatting issues, and structural problems.

**STEPS:**
- Read the entire document and fully understand its content
- Remove strange line breaks that disrupt formatting
- Add capitalization, punctuation, line breaks, and paragraphs where necessary
- **CRITICAL**: Do NOT change any content or spelling whatsoever

**OBJECTIVE:**
Clean up formatting and structure while preserving all original content exactly as written.

## Context
- **Best for**: OCR text, copied web content, malformatted documents, transcripts
- **Avoid when**: Already well-formatted text, intentional formatting choices, poetry with specific line breaks
- **Typical length**: Reformatted version of input text with improved readability

## Variables
- `{broken_text}`: Text that needs formatting cleanup

## Example Usage
**Input**: "this is some text that has weird line\nbreaks and no proper\npunctuation or capitalization"
**Output**: "This is some text that has weird line breaks and no proper punctuation or capitalization."

## Effectiveness
Rating: ⭐⭐⭐⭐⭐
Last updated: 2025-07-27

## Key Features
- **Preserves Content**: Never changes words, spelling, or meaning
- **Fixes Structure**: Corrects line breaks and paragraph formatting
- **Adds Punctuation**: Inserts proper capitalization and punctuation
- **Maintains Intent**: Respects the original author's intended message

## Variations
- Academic text: Focus on formal formatting and paragraph structure
- Casual content: Maintain conversational tone while fixing technical issues
- Technical documentation: Preserve code snippets and technical formatting

## Output Instructions
- Output the full, properly-formatted text
- Do not include warnings, notes, or explanations
- Preserve all original content exactly
- Focus only on formatting improvements