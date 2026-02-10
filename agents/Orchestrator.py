# agents/orchestrator.py

from typing import Dict, Any, Literal
from datetime import datetime
import uuid
import json


Route = Literal[
    "STUDENT_LEARNING_AGENT",
    "ASSESSMENT_AGENT",
    "COMPLIANCE_GUARD",
    "HUMAN"
]


class Orchestrator:
    """
    Orchestrator = Policy Engine

    Responsibilities:
    - Validate state
    - Decide routing
    - Merge agent outputs
    - Decide HITL escalation
    - Emit auditable decisions
    """

    def __init__(self, state_schema: Dict[str, Any]):
        self.schema = state_schema

    # ------------------------------------------------------------------
    # 1. STATE VALIDATION
    # ------------------------------------------------------------------
    def validate_state(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enforce schema and drop unknown fields.
        """
        validated_state = {}

        for field in self.schema:
            if field in state:
                validated_state[field] = state[field]

        return validated_state

    # ------------------------------------------------------------------
    # 2. ROUTING LOGIC (LangGraph Conditional Node)
    # ------------------------------------------------------------------
    def route(self, state: Dict[str, Any]) -> Route:
        """
        Decide next node in the graph.
        """

        if state.get("hitl_required", False):
            return "HUMAN"

        if state.get("needs_assessment", False):
            return "ASSESSMENT_AGENT"

        return "STUDENT_LEARNING_AGENT"

    # ------------------------------------------------------------------
    # 3. HITL DECISION
    # ------------------------------------------------------------------
    def evaluate_hitl(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determine whether human intervention is required.
        """
        mastery = state.get("mastery_score", 1.0)
        attempts = state.get("attempt_count", 0)

        if mastery < 0.35 and attempts >= 3:
            state["hitl_required"] = True

        return state

    # ------------------------------------------------------------------
    # 4. STATE MERGE RULES
    # ------------------------------------------------------------------
    def merge_state(
        self,
        previous_state: Dict[str, Any],
        agent_update: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Merge agent output into state safely.
        """
        merged_state = previous_state.copy()

        for key, value in agent_update.items():
            # Protected fields
            if key in {"student_id", "current_subject"}:
                continue

            merged_state[key] = value

        merged_state = self.evaluate_hitl(merged_state)
        return self.validate_state(merged_state)

    # ------------------------------------------------------------------
    # 5. DECISION LOGGING (Audit + LangSmith Friendly)
    # ------------------------------------------------------------------
    def log_decision(
        self,
        state: Dict[str, Any],
        route: Route,
        notes: str = ""
    ) -> None:
        """
        Append decision log for traceability.
        """
        log_entry = {
            "decision_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "route": route,
            "notes": notes,
            "state_snapshot": state,
        }

        with open("memory/decisions_log.json", "a", encoding="utf-8") as f:
