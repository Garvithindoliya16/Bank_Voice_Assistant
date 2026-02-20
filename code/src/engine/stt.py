import vosk
import sys
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time

# ... (Vosk model loading code here) ...
model = Model("models/vosk-model-small-hi-0.22")
rec = KaldiRecognizer(model,16000)

def listen():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    
    rec = vosk.KaldiRecognizer(model, 16000)
    
    print("Listening...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if text:
                return text  # THIS is what we need to return
