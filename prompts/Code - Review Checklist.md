# Code - Review Checklist

## Prompt
```
Please review this code using a comprehensive checklist approach. Analyze the following:

**Code to review**:
```{programming_language}
{code_snippet}
```

**Context**: {purpose_and_requirements}

**Review areas**:

1. **Functionality**: Does it work as intended? Edge cases covered?
2. **Readability**: Clear naming, appropriate comments, logical structure?
3. **Performance**: Efficient algorithms, unnecessary operations, bottlenecks?
4. **Security**: Input validation, SQL injection risks, data exposure?
5. **Maintainability**: Modular design, follows patterns, easy to modify?
6. **Testing**: Testable structure, missing test cases?
7. **Standards**: Coding conventions, style guide compliance?

**Output format**:
- ✅ **Strengths**: What's done well
- ⚠️ **Issues**: Problems that should be addressed
- 💡 **Suggestions**: Improvements and optimizations
- 🔧 **Action items**: Specific changes to make

Rate overall code quality: 1-10 scale with justification.
```

## Context
- **Best for**: Code review preparation, learning from examples
- **Avoid when**: Very large codebases (break into smaller chunks)
- **Typical length**: 200-500 word analysis

## Variables
- `{programming_language}`: python, javascript, java, etc.
- `{code_snippet}`: The actual code to review
- `{purpose_and_requirements}`: What the code is supposed to do

## Example Usage
**Input**:
```python
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

**Output**: Analysis covering input validation, edge cases, naming conventions, and potential improvements.

## Effectiveness
Rating: ⭐⭐⭐⭐⭐
Last updated: 2025-07-27

## Variations
- **Security focus**: Add "Prioritize security vulnerabilities and risks"
- **Performance focus**: Add "Focus on optimization opportunities"
- **Beginner friendly**: Add "Explain concepts for learning purposes"