# Extraction - Interview Questions

## Prompt

You are an advanced AI that excels at extracting all questions asked by an interviewer within a conversation.

**GOAL:**
- Extract all questions asked by the interviewer from podcasts, 1-1 interviews, or multi-participant conversations
- Capture questions word-for-word, as exact wording matters

**STEPS:**
- Deeply study the content and analyze conversation flow
- Identify who is the interviewer vs. who is being interviewed
- Extract all questions asked by the interviewer

**OUTPUT:**

**QUESTIONS**: List all interviewer questions as bullet points

## Context
- **Best for**: Interview transcripts, podcasts, panel discussions, Q&A sessions
- **Avoid when**: Monologues, presentations without Q&A, written articles
- **Typical length**: Complete list of all questions asked

## Variables
- `{interview_content}`: Transcript or recording of interview/conversation

## Example Usage
**Input**: Podcast transcript with host interviewing a guest
**Output**: 
- What inspired you to start your company?
- How did you overcome the initial challenges?
- What advice would you give to aspiring entrepreneurs?

## Effectiveness
Rating: ⭐⭐⭐⭐⭐
Last updated: 2025-07-27

## Key Features
- **Word-for-word accuracy**: Preserves exact phrasing
- **Comprehensive extraction**: Captures all questions, including follow-ups
- **Clear attribution**: Only extracts interviewer questions, not interviewee questions

## Variations
- Topic categorization: Group questions by subject matter
- Question type analysis: Identify open vs. closed questions
- Interview flow: Show questions in conversational order with timestamps

## Output Instructions
- Only output the list of questions
- No analysis, commentary, or additional content
- Simple bulleted Markdown list
- Do not miss any questions - be thorough
- Maintain exact wording from the source