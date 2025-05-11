import time
import numpy as np
import sounddevice as sd
import scipy.io.wavfile
import tempfile
import os

from pythonosc.udp_client import SimpleUDPClient
from basic_pitch.inference import predict


DURATION = 1.0 
SAMPLE_RATE = 22050
OSC_IP = "127.0.0.1"
OSC_PORT = 8000
client = SimpleUDPClient(OSC_IP, OSC_PORT)



print("\n=== Available audio devices ===\n")
devices = sd.query_devices()
for idx, d in enumerate(devices):
    io = []
    if d['max_input_channels'] > 0:
        io.append("in")
    if d['max_output_channels'] > 0:
        io.append("out")
    tag = ">" if idx == sd.default.device[0] else " "
    print(f"{tag} {idx}: {d['name']} ({', '.join(io)})")

# Choix du périphérique
device_index = input("\nEnter device index : ")
try:
    device_index = int(device_index)
    sd.default.device = (device_index, None)
    print(f"✅ Selected device : {devices[device_index]['name']}\n")
except:
    print("❌ Invalid index, fallback to default device.\n")

print("Sending via OSC... Ctrl+C to stop.")

try:
    while True:
        # Recording
        audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()

        # Temp file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            scipy.io.wavfile.write(tmp.name, SAMPLE_RATE, audio)
            tmp_path = tmp.name

        # Inference
        model_output, midi_data, note_events = predict(tmp_path)
        os.remove(tmp_path)
        for note in note_events:
            pitch, start, end, *_ = note
            client.send_message("/note", [
                int(pitch),
                float(round(start, 3)),
                float(round(end, 3))
            ])

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopping script.")