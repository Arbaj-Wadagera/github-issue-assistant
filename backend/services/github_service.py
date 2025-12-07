# File: backend/services/github_service.py
import requests
from urllib.parse import urlparse

def parse_github_url(url: str):
    """Extracts owner and repo from https://github.com/owner/repo"""
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub URL format.")
    return path_parts[0], path_parts[1]

def fetch_issue_data(repo_url: str, issue_number: int):
    owner, repo = parse_github_url(repo_url)
    
    # Using public API (rate limits apply without token)
    # Ideally, add headers={'Authorization': 'token YOUR_GITHUB_TOKEN'} if you have one
    issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    
    response = requests.get(issue_url)
    if response.status_code != 200:
        raise Exception(f"GitHub API Error: {response.status_code} - {response.text}")
        
    data = response.json()
    
    # Fetch comments to add context
    comments_url = data.get("comments_url")
    comments_data = []
    if comments_url:
        c_resp = requests.get(comments_url)
        if c_resp.status_code == 200:
            comments_data = c_resp.json()

    # Combine comments into a single string
    comments_text = "\n".join([f"- {c['body']}" for c in comments_data])
    
    return {
        "title": data.get("title"),
        "body": data.get("body"),
        "comments": comments_text
    }