import pvporcupine, json
from pvrecorder import PvRecorder

# Ключ API
with open('../key.json', 'r') as file:
    key_data = json.load(file)
    access_key = key_data["picovoice_key"]

keywords = ["../voice/aurora.ppn"]

porcupine = pvporcupine.create(access_key=access_key, keyword_paths=keywords)
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recoder.start()

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print(f"Detected 'Hi Aurora'")


except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()