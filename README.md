# 🎤 Voice Conversational AI Agent

A modular **Voice-based Conversational AI system** built in Python that integrates:

- Speech-to-Text (Whisper)
- Tool-using AI Agent
- Local LLM (Ollama)
- Text-to-Speech
- Streamlit UI

This project demonstrates an **agentic AI architecture** suitable for real-world business use cases.

---

## 🚀 Features

- 🎙️ Voice input using microphone  
- 🧠 AI agent with tool-calling logic  
- ➗ Calculator tool  
- 📄 PDF reader tool  
- 🗣️ Voice output (TTS)  
- 💬 Streamlit web UI  
- 🧩 Modular, scalable architecture  

---

## 🧱 Architecture
User (Voice)
│
▼
Speech-to-Text (Whisper)
│
▼
Agent Controller
│
├── Calculator Tool
├── PDF Reader Tool
└── LLM (Ollama)
│
▼
Text-to-Speech
│
▼
User (Voice Output)


---

## 🤖 Agent Design

The agent follows a simple reasoning loop:

1. Accepts user input (text from speech)
2. Decides:
   - Use a tool (calculator / pdf reader)
   - OR send to LLM
3. Executes tool if needed
4. Returns final response
5. Sends response to TTS

### Agent Responsibilities
- Intent detection  
- Tool selection  
- Response formatting  
- Error handling  

---

## 🗂️ Project Structure
voice_agent/
│
├── app/
│ ├── stt/ # Speech-to-text (Whisper)
│ ├── tts/ # Text-to-speech
│ ├── llm/ # Ollama client
│ ├── agent/ # Agent controller
│ ├── tools/ # Calculator, PDF reader
│ ├── memory/ # Short-term memory
│ └── ui/ # Streamlit UI
│
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/rajeshvhanakade/voice-conversational-ai.git
cd voice-conversational-ai

2. Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies

pip install -r requirements.txt

4.Run CLI Voice Agent

python main.py

5. Run Streamlit UI

streamlit run app/ui/app.py


🛠️ Tech Stack

Python 3.10+

OpenAI Whisper

Ollama (Mistral / LLaMA models)

Streamlit

Pyttsx3

SoundDevice

NumPy

📌 Example Commands

"Read pdf file"

"What is AI?"

"Exit"

👨‍💻 Author

Rajesh Vhankade
AI/ML Engineer 
