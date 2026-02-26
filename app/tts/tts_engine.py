import pyttsx3

def speak(text: str):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 160)   # speed of speech
        engine.setProperty("volume", 1.0) # max volume

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print(f"TTS error: {e}")