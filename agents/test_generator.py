from core.state import WorkflowState

def generate_tests(state: WorkflowState) -> dict:
    print(f"Agent: Generating tests for requirement: {state['requirement_text'][:30]}...")
    # Mock LLM call
    mock_test_code = """
def test_authentication():
    assert authenticate('user', 'pass') == True
"""
    return {
        "generated_tests": mock_test_code,
        "status": "reviewing"
    }
