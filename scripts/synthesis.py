from elevenlabs import play, Voice, VoiceSettings
from elevenlabs.client import ElevenLabs
from client import connect
import asyncio
from playsound import playsound
import random

# Файлы голоса
voice = [
    {'ActiveOne': '../voice/activationOne.mp3',
    'ActiveTwo': '../voice/activationTwo.mp3'},

    {'CompleteOne': '../voice/completingOne.mp3',
    'CompleteTwo': '../voice/completingTwo.mp3'}
]

# Ключ API
with open('../key.txt', 'r') as file:
    key = file.read().strip()
client = ElevenLabs(api_key=key,)


# Первичный синтез
def synthesisOne(select):
    randomKey = random.choice(list(voice[select].keys()))
    audio = voice[select][randomKey]
    playsound(audio)

# Вторичный синтез
def synthesisTwo(text):
    audio = client.generate(
    text=text,
    voice=Voice(
        voice_id='CyvhG5XCUhl0VdMRKnDN',
        settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=True)
    ),
    model="eleven_multilingual_v2"
    )
    play(audio)


# Главная функция
async def main():
    result = await connect(type="passive")

    if result[0] == "synthesis":
        if result[3] == "0":
            synthesisOne(int(result[2]))
        if result == "1":
            synthesisTwo(result[2])

while True:
    asyncio.run(main())