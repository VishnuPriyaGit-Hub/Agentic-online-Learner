# Perceive Prompt

## Purpose
Infer the current learning state of a user.

## Inputs
- User role (student / teacher / parent)
- Topic selected
- Past performance
- Recent interactions

## Output (State Estimation)
- Student mastery level per topic
- Learning gaps
- Confidence indicators
- Risk flags (low improvement, confusion)

## Example
Student struggles with fraction word problems → detect conceptual gap, not arithmetic gap.
## Tracing Notes
Each Perceive invocation logs:
- Input signals used
- State variables inferred
- Confidence score

Low confidence automatically flags HITL.
