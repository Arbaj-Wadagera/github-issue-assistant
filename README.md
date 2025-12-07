# 🤖 AI-Powered GitHub Issue Assistant

A full-stack application that uses **FastAPI**, **Streamlit**, and **OpenAI** to fetch GitHub issues, analyze them, and generate intelligent summaries and prioritization suggestions.

## 🚀 Features
* **Issue Fetching:** Automatically pulls issue details (title, body, comments) from any public GitHub repository.
* **AI Analysis:** Uses OpenAI to summarize the issue and suggest technical solutions.
* **Priority Scoring:** Auto-evaluates the urgency and impact of the issue.
* **Clean UI:** Built with Streamlit for a responsive, dark-mode friendly interface.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** FastAPI, Uvicorn
* **AI Engine:** OpenAI (GPT-3.5/4)
* **GitHub API:** For fetching repository data

## ⚙️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Arbaj-Wadagera/github-issue-assistant.git](https://github.com/Arbaj-Wadagera/github-issue-assistant.git)
    cd github-issue-assistant
    ```

2.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API Key:
    ```env
    OPENAI_API_KEY=sk-your-key-here
    GITHUB_TOKEN=your-optional-github-token
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    You need two terminals to run the app:

    *Terminal 1 (Backend):*
    ```bash
    python -m uvicorn backend.main:app --reload
    ```

    *Terminal 2 (Frontend):*
    ```bash
    python -m streamlit run frontend/ui.py
    ```

## 📸 Usage
Enter a GitHub repository URL (e.g., `https://github.com/fastapi/fastapi`) and an Issue Number. The AI will provide a concise summary and suggested next steps.
