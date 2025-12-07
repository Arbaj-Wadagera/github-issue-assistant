# 🤖 AI-Powered GitHub Issue Assistant

A full-stack application that uses **FastAPI**, **Streamlit**, and **OpenAI** to automatically analyze GitHub issues, providing intelligent summaries and prioritization scores to help developers save time.

## 🚀 Features
* **Smart Summarization:** Instantly condenses long issue threads into key points.
* **Priority Scoring:** AI evaluates urgency (High/Medium/Low) based on context.
* **Solution Suggestions:** Proposes potential technical fixes for the reported bug.
* **Modern UI:** Clean, dark-mode friendly interface built with Streamlit.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Backend:** FastAPI (Python)
* **AI Engine:** OpenAI GPT Models
* **Data:** GitHub REST API

## ⚙️ Setup & Installation

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Arbaj-Wadagera/github-issue-assistant.git](https://github.com/Arbaj-Wadagera/github-issue-assistant.git)
    cd github-issue-assistant
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables**
    Create a `.env` file and add your OpenAI Key:
    ```
    OPENAI_API_KEY=sk-your-key-here
    ```

4.  **Run the App**
    You need 2 terminals:
    * **Backend:** `python -m uvicorn backend.main:app --reload`
    * **Frontend:** `python -m streamlit run frontend/ui.py`