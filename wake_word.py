import sounddevice as sd
import numpy as np
import speech_recognition as sr

WAKE_WORD = "hello"  # Change this to your wake word

def detect_wake_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Umm ... I am listening ...")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()

                if WAKE_WORD in text:
                    print(f"Wake word '{WAKE_WORD}' detected! Activating assistant...")
                    return True  # Signal that wake word is detected

            except sr.UnknownValueError:
                continue  # Ignore unrecognized speech
            except sr.RequestError:
                print("Speech recognition API unavailable.")

if __name__ == "__main__":
    if detect_wake_word():
        print("You can now proceed with your main.py functionality.")
