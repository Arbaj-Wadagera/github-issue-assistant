# File: backend/schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional

class IssueRequest(BaseModel):
    repo_url: str
    issue_number: int

# Matches the "Required AI-Generated JSON Output Format" from the prompt
class IssueAnalysis(BaseModel):
    summary: str = Field(..., description="A one-sentence summary of the problem")
    type: str = Field(..., description="bug, feature_request, documentation, question, or other")
    priority_score: int = Field(..., description="Score from 1 (low) to 5 (critical)")
    priority_justification: str = Field(..., description="Brief justification for the score")
    suggested_labels: List[str] = Field(..., description="Array of 2-3 relevant GitHub labels")
    potential_impact: Optional[str] = Field(None, description="Impact on users if it is a bug")