# main.py

import sys
from pathlib import Path

# Add app/ to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent / "app"
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from stt.whisper_stt import listen
from agent.controller import agent_loop
from tts.tts_engine import speak


def main():
    print("🎤 Voice agent started. Say 'exit' to quit.")

    while True:
        try:
            user_text = listen()
            print("You:", user_text)

            if not user_text:
                continue

            if "exit" in user_text.lower():
                print("Exiting...")
                break

            reply = agent_loop(user_text)
            print("AI:", reply)

            speak(reply)

        except KeyboardInterrupt:
            print("\nStopped by user.")
            break

        except Exception as e:
            print("⚠️ Error:", e)


if __name__ == "__main__":
    main()