from core.graph import app
import pytest

@pytest.mark.asyncio
async def test_successful_workflow():
    state = {
        "requirement_text": "Create a login test",
        "generated_tests": "",
        "review_comments": [],
        "status": "pending",
        "retry_count": 0
    }
    
    result = await app.ainvoke(state)
    assert result["status"] == "approved"
    assert "test_authentication" in result["generated_tests"]
