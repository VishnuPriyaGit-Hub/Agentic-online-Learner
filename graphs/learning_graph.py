 # graph/learning_graph.py

from typing import Dict, Any
from langgraph.graph import StateGraph, END

from agents.orchestrator import Orchestrator
from agents.student_learning_agent import student_learning_agent
from agents.assessment_agent import assessment_agent
from agents.compliance_guard import compliance_guard

# ---------------------------------------------------------
# 1. Define State Type (Shared Across Graph)
# ---------------------------------------------------------
State = Dict[str, Any]

# ---------------------------------------------------------
# 2. Initialize Orchestrator
# ---------------------------------------------------------
STATE_SCHEMA = {
    "student_id": str,
    "current_subject": str,
    "current_topic": str,
    "mastery_score": float,
    "attempt_count": int,
    "needs_assessment": bool,
    "hitl_required": bool,
}

orchestrator = Orchestrator(state_schema=STATE_SCHEMA)

# ---------------------------------------------------------
# 3. Wrap Agents as Graph Nodes
# ---------------------------------------------------------
def orchestrator_node(state: State) -> State:
    """
    Entry point + policy evaluation.
    """
    state = orchestrator.validate_state(state)
    orchestrator.log_decision(state, route="ORCHESTRATOR")
    return state


def student_learning_node(state: State) -> State:
    update = student_learning_agent(state)
    return orchestrator.merge_state(state, update)


def assessment_node(state: State) -> State:
    update = assessment_agent(state)
    return orchestrator.merge_state(state, update)


def compliance_node(state: State) -> State:
    update = compliance_guard(state)
    return orchestrator.merge_state(state, update)


def human_node(state: State) -> State:
    """
    Placeholder for HITL.
    Actual UI / approval comes later.
    """
    state["hitl_required"] = False
    state["needs_assessment"] = False
    return state


# ---------------------------------------------------------
# 4. Build LangGraph
# ---------------------------------------------------------
def build_learning_graph():
    graph = StateGraph(State)

    # Nodes
    graph.add_node("orchestrator", orchestrator_node)
    graph.add_node("student_learning", student_learning_node)
    graph.add_node("assessment", assessment_node)
    graph.add_node("compliance", compliance_node)
    graph.add_node("human", human_node)

    # Entry
    graph.set_entry_point("orchestrator")

    # Routing logic (Orchestrator decides)
    graph.add_conditional_edges(
        "orchestrator",
        orchestrator.route,
        {
            "STUDENT_LEARNING_AGENT": "student_learning",
            "ASSESSMENT_AGENT": "assessment",
            "HUMAN": "human",
        },
    )

    # Normal flow
    graph.add_edge("student_learning", "compliance")
    graph.add_edge("assessment", "compliance")

    # Compliance can loop back or end
    graph.add_conditional_edges(
        "compliance",
        lambda state: "HUMAN" if state.get("hitl_required") else END,
        {
            "HUMAN": "human",
            END: END,
        },
    )

    # Human always returns to orchestrator
    graph.add_edge("human", "orchestrator")

    return graph.compile()
