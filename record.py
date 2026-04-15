import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # sample rate
seconds = 5  # duration

print("🎤 Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("input.wav", fs, recording)
print("✅ Recording saved as input.wav")