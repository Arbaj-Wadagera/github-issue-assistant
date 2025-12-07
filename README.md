# 🤖 AI-Powered GitHub Issue Assistant

A full-stack application that uses **FastAPI**, **Streamlit**, and **OpenAI** to automatically analyze GitHub issues — providing intelligent summaries, priority scores, and actionable insights.

---

## 📌 Features

- **Smart Summarization:** Condenses long issue threads into clear, essential points.  
- **Priority Scoring:** AI evaluates urgency (High / Medium / Low) based on issue context.  
- **Solution Suggestions:** Recommends potential technical fixes automatically.  
- **Modern UI:** Clean, dark-mode-friendly interface built with Streamlit.

---

## 🧰 Tech Stack

| Layer       | Technology |
|------------|------------|
| Frontend   | Streamlit (Python) |
| Backend    | FastAPI (Python) |
| AI Engine  | OpenAI GPT Models |
| Data       | GitHub REST API |

---

## ⚙️ Setup & Installation

> You will use **two separate terminals** throughout the setup.

---

## 🖥️ 1. Terminal 1 — Project Setup & Dependencies

Open your first terminal (**T1**) and run:

```bash
# Clone the repository
git clone https://github.com/Arbaj-Wadagera/github-issue-assistant.git

# Navigate to the directory
cd github-issue-assistant

# Install dependencies
pip install -r requirements.txt
```

### 🔑 Configure OpenAI API Key

1. **Generate an API key:**  
   https://platform.openai.com/api-keys

2. **Create a `.env` file** by running (in T1):

    ```cmd
    notepad .env
    ```

3. **Paste your API key** into the file:

    ```env
    OPENAI_API_KEY=sk-your-key-here
    ```

Save and close the Notepad window.

---

## 🚀 2. Running the Application

### ▶️ Step 1 — Start Backend (Terminal 1)

Run the FastAPI backend:

```bash
python -m uvicorn backend.main:app --reload
```

---

### ▶️ Step 2 — Start Frontend (Terminal 2)

Open a **second terminal (T2)** and run:

```bash
# Navigate to the project folder
cd github-issue-assistant

# Launch Streamlit UI
python -m streamlit run frontend/ui.py
```

---

## 🧪 3. Usage

Once both terminals are running:

1. Streamlit will open automatically (or visit `http://localhost:8501`).
2. **Refresh the page** after startup.
3. Start entering GitHub issue URLs to analyze them with AI.

---

## ✔️ You're Ready to Go!

Your AI-powered GitHub Issue Assistant is now live and ready to analyze issues, generate summaries, prioritize tasks, and offer smart recommendations.

