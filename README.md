# HUMN1

## Installation

### Create Virtual Environment

Before installing dependencies, it is recommended to create a virtual environment:

```bash
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (Linux/Mac)
venv\Scripts\activate  # Activate the virtual environment (Windows)
```

### Linux Installation

Run the following commands to install dependencies:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip mpg321 portaudio19-dev
pip install sounddevice numpy openai-whisper ollama gtts
```

### Windows Installation

Run the following commands in Command Prompt (as administrator):

```powershell
pip install sounddevice numpy openai-whisper ollama gtts
```

Additionally, install a media player like VLC if Windows doesn't support MP3 playback.

## Usage

Run the script using:

```bash
python voice_to_text_ai.py
```

## Dependencies

- Python 3+
- `sounddevice` (for recording audio)
- `numpy` (for handling audio data)
- `wave` (default in Python, for saving `.wav` files)
- `whisper` (for speech-to-text processing)
- `ollama` (for AI responses)
- `gtts` (for text-to-speech conversion)
- `mpg321` (Linux) or an MP3 player (Windows)

## Notes

- Ensure you have a working microphone for recording.
- The script defaults to a 5-second recording duration but can be modified.
- For better transcription accuracy, consider downloading Whisper's larger models.

## License

This project is free to use and modify.

