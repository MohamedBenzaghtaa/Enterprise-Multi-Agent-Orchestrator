from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.graph import app as agent_workflow

app = FastAPI(title="Multi-Agent Orchestrator API")

class RequirementRequest(BaseModel):
    text: str

class WorkflowResponse(BaseModel):
    tests: str
    status: str
    comments: list[str]

@app.post("/api/v1/orchestrate", response_model=WorkflowResponse)
async def trigger_workflow(req: RequirementRequest):
    initial_state = {
        "requirement_text": req.text,
        "generated_tests": "",
        "review_comments": [],
        "status": "pending",
        "retry_count": 0
    }
    
    try:
        final_state = await agent_workflow.ainvoke(initial_state)
        return WorkflowResponse(
            tests=final_state["generated_tests"],
            status=final_state["status"],
            comments=final_state["review_comments"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
