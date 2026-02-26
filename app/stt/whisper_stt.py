import os
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Make sure ffmpeg is found
os.environ["PATH"] += r";C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin"

# Load model once
model = whisper.load_model("base")

def listen(seconds: int = 5) -> str:
    fs = 16000

    try:
        print("Listening...")
        audio = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype="float32"
        )
        sd.wait()

        wav.write("temp.wav", fs, audio)

        result = model.transcribe("temp.wav")
        text = result.get("text", "").strip()

        if not text:
            return "⚠️ I could not hear anything."

        return text

    except Exception as e:
        return f"⚠️ Microphone error: {e}"