

<h1>🎙️ Voice Conversational AI Agent</h1>

<p>
A fully local <strong>Voice Conversational AI Agent</strong> built with Python that enables users to interact with an AI system using speech.
The system converts voice input into text (Speech-to-Text), processes it using a local Large Language Model (LLM),
and responds using synthesized speech (Text-to-Speech).
</p>

<div class="section">
    <span class="badge">Python</span>
    <span class="badge">Whisper STT</span>
    <span class="badge">Local LLM</span>
    <span class="badge">TTS</span>
    <span class="badge">Streamlit</span>
</div>

<hr>

<div class="section">
<h2>🚀 Features</h2>
<ul>
    <li>🎤 Speech-to-Text (STT) using Whisper</li>
    <li>🧠 Local LLM-based response generation</li>
    <li>🔊 Text-to-Speech (TTS) voice output</li>
    <li>💬 Multi-turn conversation handling</li>
    <li>🗂 Modular architecture (STT, LLM, TTS, Controller)</li>
    <li>🖥️ Streamlit user interface</li>
    <li>⚡ Runs fully offline (no cloud APIs required)</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🧠 System Architecture</h2>

<pre>
User Voice
   │
   ▼
Speech-to-Text (Whisper)
   │
   ▼
LLM (Local Model)
   │
   ▼
Text-to-Speech (TTS)
   │
   ▼
Audio Response
</pre>
</div>

<hr>

<div class="section">
<h2>📁 Project Structure</h2>

<pre>
voice_agent/
│
├── app/
│   ├── stt/            # Speech-to-Text module
│   ├── tts/            # Text-to-Speech module
│   ├── llm/            # LLM client
│   ├── agent/          # Conversation controller
│   ├── tools/          # Utility tools
│
├── models/             # Local LLM models
├── ui/
│   └── app.py          # Streamlit UI
├── main.py
└── README.html
</pre>
</div>

<hr>

<div class="section">
<h2>⚙️ Installation</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/your-username/voice-agent.git
cd voice-agent
</pre>

<h3>2️⃣ Create Virtual Environment</h3>
<pre>
python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)
</pre>

<h3>3️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>
</div>

<hr>

<div class="section">
<h2>🤖 Model Setup</h2>

<ol>
    <li>Download a Whisper model for STT</li>
    <li>Download a GGUF local LLM model (e.g., Mistral or Llama)</li>
    <li>Place models inside the <code>models/</code> directory</li>
</ol>

</div>

<hr>

<div class="section">
<h2>▶️ Run the Application</h2>

<pre>
streamlit run app/ui/app.py
</pre>

<p>
or
</p>

<pre>
python main.py
</pre>

</div>

<hr>

<div class="section">
<h2>🧪 Example Workflow</h2>
<ol>
    <li>User speaks into microphone</li>
    <li>Speech is converted to text (STT)</li>
    <li>Text is sent to LLM for response</li>
    <li>Response is converted to audio (TTS)</li>
    <li>Audio response is played back to user</li>
</ol>
</div>

<hr>

<div class="section">
<h2>🛠 Technology Stack</h2>
<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>OpenAI Whisper (STT)</li>
    <li>Llama.cpp (Local LLM)</li>
    <li>Edge-TTS / PyTTSx3 (TTS)</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🔐 Key Design Principles</h2>
<ul>
    <li>Offline-first architecture</li>
    <li>Modular design for easy extensibility</li>
    <li>Separation of concerns (STT, LLM, TTS)</li>
    <li>Business-oriented conversational flow</li>
</ul>
</div>


<div class="section">
<h2>📜 License</h2>
<p>
This project is licensed under the MIT License.
</p>
</div>

<hr>


</body>
</html>
