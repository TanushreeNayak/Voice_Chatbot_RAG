import sounddevice as sd
from scipy.io.wavfile import write
import requests

# Step 1: Record audio
fs = 16000
seconds = 15

print("🎤 Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("input.wav", fs, recording)
print("✅ Recorded")

# Step 2: Send to API
url = "http://127.0.0.1:5000/voice"

files = {
    "audio": open("input.wav", "rb")
}

response = requests.post(url, files=files)

print("🤖 Response:", response.text)