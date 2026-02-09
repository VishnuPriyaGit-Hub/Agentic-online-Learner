# System Architecture

# Agentic Learner – System Architecture

## High-Level Agent Interaction Flow

```mermaid
flowchart TD
    User --> Orchestrator
    Orchestrator --> AssessmentAgent
    AssessmentAgent --> ComplianceGuard
    ComplianceGuard -->|HITL Required| Human
    Human -->|Approve| Orchestrator
    Human -->|Reject| Orchestrator
 

Human-in-the-loop checkpoints enforce safety.
## Observability Architecture

### LangSmith Tracing
Each interaction produces a trace capturing:
- Agent invoked
- Prompt used (Perceive / Plan / Act)
- Tools called
- Outputs generated
- Errors or retries

Traces are grouped by:
- Student ID (hashed)
- Class ID
- Session ID

### Logging Strategy
Logs record:
- High-impact decisions
- HITL interruptions
- Agent failures
- Escalations

No raw student answers or PII are stored.
