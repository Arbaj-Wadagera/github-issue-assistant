# File: backend/services/llm_service.py
import os
import json
import openai
from dotenv import load_dotenv
from backend.utils.prompt_templates import SYSTEM_PROMPT, get_analysis_prompt
from backend.schemas import IssueAnalysis

load_dotenv() # Load API Key from .env

# Initialize Client (Assumes OPENAI_API_KEY is in .env)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_issue(title: str, body: str, comments: str) -> dict:
    prompt = get_analysis_prompt(title, body, comments)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cost-effective and fast model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0, # Deterministic output for consistent JSON
            response_format={"type": "json_object"} # Forces JSON mode
        )
        
        content = response.choices[0].message.content
        return json.loads(content)
        
    except Exception as e:
        print(f"LLM Error: {e}")
        # Return a fallback or re-raise
        raise e