from typing import TypedDict, Annotated, Sequence
import operator

class WorkflowState(TypedDict):
    requirement_text: str
    generated_tests: str
    review_comments: Annotated[Sequence[str], operator.add]
    status: str # 'pending', 'generating', 'reviewing', 'approved', 'failed'
    retry_count: int
