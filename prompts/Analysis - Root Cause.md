# Analysis - Root Cause

## Prompt
```
I need help analyzing a problem using root cause analysis. Here's the situation:

**Problem**: {describe_the_problem}

**Context**: {relevant_background_information}

**What I've observed**: {symptoms_and_evidence}

Please help me:
1. Identify potential root causes using the "5 Whys" method
2. Categorize causes (people, process, technology, environment)
3. Rank causes by likelihood and impact
4. Suggest investigation steps to validate the most likely causes
5. Recommend preventive measures

Focus on actionable insights rather than theoretical analysis.
```

## Context
- **Best for**: Complex problems with multiple contributing factors
- **Avoid when**: Simple issues with obvious solutions
- **Typical length**: 300-800 word analysis

## Variables
- `{describe_the_problem}`: Clear, specific problem statement
- `{relevant_background_information}`: Context that might influence the analysis
- `{symptoms_and_evidence}`: Observable facts and data

## Example Usage
**Input**: 
```
Problem: Website performance has degraded 40% over the past month
Context: Recent deployment of new features, increased user traffic
What I've observed: Slow page loads, database timeout errors, user complaints
```

**Output**: Structured analysis with potential causes like database optimization needs, code inefficiencies, infrastructure scaling issues, etc.

## Effectiveness
Rating: ⭐⭐⭐⭐⭐
Last updated: 2025-07-27

## Variations
- **Technical focus**: Add "Prioritize technical causes and solutions"
- **Business focus**: Add "Consider business impact and stakeholder perspectives"
- **Quick version**: Skip detailed categorization, focus on top 3 causes