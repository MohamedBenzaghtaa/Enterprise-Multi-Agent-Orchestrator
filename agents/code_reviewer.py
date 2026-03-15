from core.state import WorkflowState

def review_tests(state: WorkflowState) -> dict:
    print("Agent: Reviewing generated tests...")
    # Mock LLM review logic
    if "assert" in state["generated_tests"]:
        return {
            "status": "approved",
            "review_comments": ["Tests look robust and meet coverage standards."]
        }
    
    return {
        "status": "failed",
        "retry_count": state["retry_count"] + 1,
        "review_comments": ["Missing assertions in test code."]
    }
