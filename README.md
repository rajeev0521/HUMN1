# HUMN1: Voice to Text AI

HUMN1 is a Python-based voice-to-text AI system that records audio, transcribes it using OpenAI's Whisper model, processes the text with the Ollama language model, and converts the response back to speech using Google Text-to-Speech (gTTS).

## Features:
- Record voice input.
- Transcribe speech to text using Whisper.
- Process the text with the Ollama AI model.
- Convert AI-generated responses back to speech.
- Auto-play the generated speech response.

## Requirements
Ensure you have the following dependencies installed before running the project.

### **Linux Installation**
```bash
# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate
```
```bash
# Install dependencies
pip install requirements -r
```
## or(any-one)
```bash
pip install sounddevice numpy wave ollama gtts whisper pydub

# Install ffmpeg for audio processing
sudo apt install ffmpeg mpg321
```

### **Windows Installation**
```powershell
# Create and activate a virtual environment
python -m venv env
env\Scripts\activate

# Install dependencies
pip install sounddevice numpy wave ollama gtts whisper pydub

# Install ffmpeg manually (Download from https://ffmpeg.org/download.html)
```

## Usage
```bash
# Activate virtual environment (Linux)
source env/bin/activate

# Activate virtual environment (Windows)
env\Scripts\activate

# Run the main script
python main.py
```

## How It Works
1. The program records audio input from the microphone and saves it as an MP3 file.
2. Whisper transcribes the recorded speech to text.
3. The text is sent to the Ollama AI model to generate a response.
4. The response is converted into speech using gTTS.
5. The generated speech is automatically played.

## Troubleshooting
- If you encounter issues with `sounddevice`, ensure your microphone is properly configured.
- If `ffmpeg` is missing, install it manually.
- On Linux, if `mpg321` fails to play audio, try `sudo apt install mpg321`.

## License
This project is open-source and available under the MIT License.

