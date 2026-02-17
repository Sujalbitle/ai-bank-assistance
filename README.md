# 🏦 AI-Powered Banking Customer Query Resolution Agent

A conversational AI agent that resolves banking customer queries using OpenAI GPT and Streamlit.

## Features

- Natural language understanding of banking queries
- Answers questions about accounts, loans, branches, transactions
- Auto-escalates complex/security queries to human agents
- Clean web interface built with Streamlit

## Tech Stack

- Python 3.10+
- OpenAI GPT-3.5 Turbo
- Streamlit (Frontend)
- Python-dotenv (Environment management)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/banking-ai-agent.git
cd banking-ai-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

## Project Structure

```
banking-ai-agent/
├── data/               # Banking knowledge documents
├── src/                # Core Python modules
│   ├── ai_agent.py     # OpenAI integration
│   ├── document_loader.py  # Document handling
│   └── escalation.py   # Escalation logic
├── app.py              # Streamlit web app
└── requirements.txt    # Dependencies
```

## Sample Queries to Test

- "What are your savings account interest rates?"
- "How do I report a stolen credit card?"
- "What documents do I need to open an account?"
- "Where is the nearest branch?"
- "How long does a wire transfer take?"
# ai-banking-assistance
