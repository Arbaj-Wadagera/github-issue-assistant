from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import IssueRequest, IssueAnalysis
from backend.services.github_service import fetch_issue_data
from backend.services.llm_service import analyze_issue

app = FastAPI(title="GitHub Issue Assistant API")

# Enable CORS (Cross-Origin Resource Sharing)
# This allows the Frontend (Port 8501) to talk to the Backend (Port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=IssueAnalysis)
async def analyze_github_issue(request: IssueRequest):
    """
    1. Fetches issue data from GitHub.
    2. Sends data to LLM for analysis.
    3. Returns structured JSON.
    """
    try:
        # Step 1: Fetch Data
        print(f"Fetching issue: {request.repo_url} #{request.issue_number}")
        issue_data = fetch_issue_data(request.repo_url, request.issue_number)
        
        # Step 2: Analyze with LLM
        print("Sending to LLM...")
        analysis_result = analyze_issue(
            title=issue_data["title"],
            body=issue_data["body"],
            comments=issue_data["comments"]
        )
        
        return analysis_result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run the server on http://localhost:8000
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)