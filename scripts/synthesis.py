from elevenlabs import play, Voice, VoiceSettings
from elevenlabs.client import ElevenLabs
from client import connect
import asyncio, random, pyglet

# Файлы голоса
voice = [
    ['../voice/activationOne.mp3',
    '../voice/activationTwo.mp3'],

    ['../voice/completingOne.mp3',
    '../voice/completingTwo.mp3'],

    ['../voice/start.mp3']
]

# Ключ API
with open('../key.txt', 'r') as file:
    key = file.read().strip()
    file.close()
client = ElevenLabs(api_key=key)


# Первичный синтез
def synthesisOne(select):
    audio = random.choice(voice[select])
    
    # Проигрывание аудиофайла
    sound = pyglet.media.load(audio, streaming=False)
    sound.play()
    pyglet.app.run()

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

    if "synthesis" in result["recipient"]:
        if result["content"][1] == "0":
            synthesisOne(int(result["content"][0]))
        elif result["content"][1] == "1":
            synthesisTwo(result["content"][0])

while True:
    asyncio.run(main())