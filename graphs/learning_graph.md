# Learning Graph Architecture

This document describes the LangGraph-based execution flow
for the Agentic Online Learner system.

---

## Purpose

The Learning Graph coordinates:
- Student learning
- Assessment
- Compliance checks
- Human-in-the-loop escalation

The Orchestrator acts as the policy engine that determines
routing and state evolution.

---

## Nodes

### Orchestrator
- Validates state
- Determines next agent
- Logs routing decisions

### Student Learning Agent
- Delivers learning content
- Updates mastery signals

### Assessment Agent
- Evaluates understanding
- Updates mastery score

### Compliance Guard
- Enforces safety and policy
- Triggers HITL when required

### Human Node
- Manual review / approval
- Resets escalation flags

---

## Routing Logic

- Orchestrator decides next node
- Compliance Guard determines termination or HITL
- Human node loops back to Orchestrator

---

## HITL Policy

Human intervention is triggered when:
- `mastery_score < 0.35`
- `attempt_count >= 3`

---

## Mermaid Diagram

```mermaid
flowchart TD
    Orchestrator --> StudentLearning
    Orchestrator --> Assessment
    StudentLearning --> ComplianceGuard
    Assessment --> ComplianceGuard
    ComplianceGuard -->|HITL| Human
    ComplianceGuard -->|Safe| End
    Human --> Orchestrator
