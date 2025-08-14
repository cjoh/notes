# Extraction - Future Predictions

## Prompt

You fully digest input and extract all predictions made within the content.

Take a step back and think step-by-step about how to achieve the best results by following the steps below.

**STEPS:**
- Extract all predictions made within the content
- For each prediction, capture:
  - The specific prediction (max 15 words)
  - The date by which it's supposed to occur
  - The confidence level given
  - How we'll know if it's true or not

**OUTPUT FORMAT:**

**PREDICTIONS**: Bulleted list of predictions (max 15 words each)

**PREDICTIONS TABLE**:
| Prediction | Confidence | Date | How to Verify |
|------------|------------|------|---------------|
| [prediction details] | [percentage/level] | [target date] | [verification method] |

## Context
- **Best for**: Futurist content, market analysis, technology forecasts, strategic planning documents
- **Avoid when**: Historical analysis, current state descriptions, opinion pieces without predictions
- **Typical length**: All predictions with structured table

## Variables
- `{content}`: Any content containing predictions about the future

## Example Usage
**Input**: Technology trends article with expert predictions
**Output**: 
**PREDICTIONS**:
- AI will surpass human intelligence in specific domains
- Quantum computing will break current encryption standards
- Self-driving cars will be mainstream in cities

**PREDICTIONS TABLE**:
| Prediction | Confidence | Date | How to Verify |
|------------|------------|------|---------------|
| AI surpasses human intelligence in domains | 85% | 2030 | Benchmark test results |
| Quantum breaks encryption | 60% | 2035 | First documented breach |
| Self-driving cars mainstream | 90% | 2028 | >50% new car sales |

## Effectiveness
Rating: ⭐⭐⭐⭐⭐
Last updated: 2025-07-27

## Variations
- Industry focus: Extract predictions for specific sectors
- Confidence analysis: Group by confidence levels
- Timeline view: Organize predictions chronologically

## Output Instructions
- Only output valid Markdown (no bold/italics)
- Maximum 15 words per prediction
- Include all four elements for each prediction
- Create clean, readable table format