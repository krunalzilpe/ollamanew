# My GPT

A Streamlit application powered by LangChain and Ollama that provides an interactive AI chatbot interface.

## Features

- Interactive chat interface built with Streamlit
- Powered by Ollama (gemma2:2b model)
- Uses LangChain for prompt management and chain orchestration

## Requirements

- Python 3.8+
- Ollama (with gemma2:2b model)

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install streamlit langchain langchain-community
```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## How it works

1. The app uses a ChatPromptTemplate to structure prompts
2. Questions are sent to the Ollama model (gemma2:2b)
3. Responses are displayed in the Streamlit interface
