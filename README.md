
🌟 Multi-LLM Chat Interface with Chainlit & OpenRouter
A conversational AI app that lets users interact with multiple LLM models (DeepSeek, Gemini, Mistral, etc.) via OpenRouter’s API, built with Chainlit for a seamless chat UI.

https://img.shields.io/badge/Demo-Coming_Soon-blue
https://img.shields.io/badge/Python-3.9+-brightgreen
https://img.shields.io/badge/Powered_by-OpenRouter-orange

🛠️ Prerequisites
Before running the app, ensure you have:

Python 3.9+ installed

An OpenRouter API key

Required Python packages

🚀 Quick Start
1. Set Up Environment
bash
git clone <your-repo-url>
cd <repo-directory>
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
2. Install Dependencies
bash
pip install chainlit python-dotenv openai
3. Configure API Key
Create a .env file in the root directory:

env
OPEN_ROUTER_API_KEY="your_openrouter_api_key_here"
4. Run the App
bash
chainlit run app.py
Open your browser at http://localhost:8000 to start chatting!

🧠 How It Works
🔄 Workflow Overview
User selects an LLM model from a dropdown (DeepSeek, Gemini, etc.).

Chat history is maintained in-session.

OpenRouter API routes queries to the selected model.

Agent processes inputs and streams responses back.

📝 Code Breakdown
1. Imports & Setup
python
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
import chainlit as cl
chainlit: Powers the chat UI.

AsyncOpenAI: Async client for OpenRouter API calls.

2. Model Configuration
python
models = {
    "DeepSeek": "deepseek/deepseek-r1:free",
    "Gemini-2-flash-exp": "google/gemini-2.0-flash-exp:free",
    # ... other models
}
Predefined list of OpenRouter-supported models.

3. Chat Initialization (@cl.on_chat_start)
Sends a welcome message.

Renders a model selection dropdown using cl.ChatSettings.

4. Model Selection Handler (@cl.on_settings_update)
Updates the session with the user’s selected model.

Confirms selection via chat message (e.g., "You’ve selected Mistral 🤖").

5. Message Processing (@cl.on_message)
Stores user input in history (list of dicts with role/content).

Initializes Agent with the selected model.

Runs sync inference via Runner.run_sync() and displays the output.

🌈 Features
Multi-LLM Support: Switch between models dynamically.

Conversational Memory: Retains chat history during the session.

Easy Setup: Configured via .env and Chainlit’s intuitive decorators.

📂 Project Structure
text
.
├── app.py                # Main application code
├── .env                  # API key configuration
├── requirements.txt      # Dependencies (generate with `pip freeze > requirements.txt`)
└── README.md             # This guide
