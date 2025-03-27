import sounddevice as sd
from pydub import AudioSegment
import numpy as np
import wave
import ollama
import os
import whisper
import tempfile
import subprocess
from gtts import gTTS
import re  # For sentence detection

# Load Whisper Model (Faster Version)
model = whisper.load_model("base.en")

def record_audio(filename="audio.wav", duration=5, samplerate=16000):
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording finished.")

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)  # Mono for speed
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

    return filename

def transcribe_audio(filename):
    print("Transcribing audio...")
    result = model.transcribe(filename)
    text = result["text"]
    print("Transcription:", text, "\n")
    return text  # Return text immediately

def query_ollama_streaming(prompt, model="llama3:latest"):
    print("Querying Ollama...")
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}], stream=True)

    sentence_buffer = ""  # Store words until a complete sentence is formed

    for chunk in response:
        chunk_text = chunk["message"]["content"]
        sentence_buffer += " " + chunk_text.strip()  # Append and clean up spaces

        # Extract complete sentences
        sentences = re.findall(r'[^.!?]*[.!?]"?', sentence_buffer)

        for sentence in sentences:
            if sentence.strip():  # Ensure non-empty
                text_to_speech(sentence.strip())  # Convert & Play
                sentence_buffer = sentence_buffer.replace(sentence, "").strip()  # Remove spoken part

    # Speak any remaining partial sentence
    if sentence_buffer.strip():
        text_to_speech(sentence_buffer.strip())

def text_to_speech(text):
    print(f"\nConverting to speech: {text}")
    tts = gTTS(text=text, lang="en")
    
    # Save audio temporarily
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)

    # Play the generated speech immediately
    play_audio(temp_audio.name)

def play_audio(filename):
    print("Playing audio...")
    if os.name == "nt":  # Windows
        os.system(f"start {filename}")
    else:  # Linux / Mac
        subprocess.call(["mpg321", filename])  # Ensure mpg321 is installed

def main():
    while True:
          audio_file = record_audio()
          text = transcribe_audio(audio_file)
          query_ollama_streaming(text)  # Stream response & speak instantly

    
  
if __name__ == "__main__":
    main()
