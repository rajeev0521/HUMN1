import sounddevice as sd
import numpy as np
import wave
import whisper
import ollama
import os
from gtts import gTTS
import tempfile
import subprocess

def record_audio(filename="recorded.wav", duration=5, samplerate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype=np.int16)
    sd.wait()
    print("Recording finished.")
    
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())
    
    return filename

def transcribe_audio(filename, model_name="base.en"):
    print("Transcribing...")
    model = whisper.load_model(model_name)
    result = model.transcribe(filename)
    print("Transcription: ", result["text"])
    return result["text"]

def query_ollama(prompt, model="llama3:latest"):
    print("Querying Ollama...")
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    response_text = response["message"]["content"]
    print("Ollama Response: ", response_text)
    return response_text

def text_to_speech(text):
    print("Converting text to speech...")
    tts = gTTS(text=text, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

def play_audio(filename):
    print("Playing audio...")
    if os.name == "nt":  # Windows
        os.system(f"start {filename}")
    else:  # Linux / Mac
        subprocess.call(["mpg321", filename])

def main():
    audio_file = record_audio()
    text = transcribe_audio(audio_file)
    response = query_ollama(text)
    audio_response = text_to_speech(response)
    play_audio(audio_response)

if __name__ == "__main__":
    main()
