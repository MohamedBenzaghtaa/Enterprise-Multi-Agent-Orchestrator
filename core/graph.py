from langgraph.graph import StateGraph, END
from core.state import WorkflowState
from agents.test_generator import generate_tests
from agents.code_reviewer import review_tests

def router(state: WorkflowState):
    if state["status"] == "approved":
        return END
    elif state["retry_count"] > 3:
        return END
    return "generate"

workflow = StateGraph(WorkflowState)

# Add nodes
workflow.add_node("generate", generate_tests)
workflow.add_node("review", review_tests)

# Define edges
workflow.set_entry_point("generate")
workflow.add_edge("generate", "review")
workflow.add_conditional_edges("review", router)

# Compile
app = workflow.compile()
