voice_agent/
│
├── __init__.py
├── app/
│   ├── __init__.py
│   ├── stt/
│   │     ├── __init__.py
│   │     └── whisper_stt.py
│   ├── tts/
│   │     ├── __init__.py
│   │     └── tts_engine.py
│   ├── llm/
│   │     ├── __init__.py
│   │     └── ollama_client.py
│   ├── agent/
│   │     ├── __init__.py
│   │     └── controller.py
│   ├── tools/
│   │     ├── __init__.py
│   │     ├── calculator.py
│   │     └── pdf_reader.py
│   ├── memory/
│   │     ├── __init__.py
│   │     └── short_term.py
│   └── ui/
│         ├── __init__.py
│         └── app.py
│
├── data/
│     ├── __init__.py
│     └── documents/
│           └── __init__.py
│
├── main.py
└── requirements.txt