import whisper
import pyttsx3

model = whisper.load_model("base")

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()