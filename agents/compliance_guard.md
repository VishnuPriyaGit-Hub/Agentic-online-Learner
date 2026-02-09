# Compliance Guard Agent

## Purpose
Act as the safety and governance layer across the agentic system.

## Human-in-the-Loop Triggers
This agent halts execution and requests human approval when:
- A final assessment or report is requested
- Curriculum standards are modified
- A student shows no improvement across multiple cycles
- Confidence in generated content is low

## Enforcement
- Blocks unauthorized actions
- Escalates ambiguous decisions
- Ensures role-based access

## Example
If an assessment agent attempts to generate a final exam,
execution is paused and routed to a human reviewer.
