from elevenlabs import play, Voice
from elevenlabs.client import ElevenLabs
from client import connect
import asyncio, random, json, playsound

# Файлы голоса
voice = [
    ['../voice/activationOne.mp3',
     '../voice/activationTwo.mp3'],
    ['../voice/completingOne.mp3',
     '../voice/completingTwo.mp3'],
    ['../voice/start.mp3']
]

# Ключ API и клиент
with open('../key.json', 'r') as file:
    key_data = json.load(file)
    api_key = key_data["elevenlabs_key"]

client = ElevenLabs(api_key=api_key)


# Первичный синтез
def synthesisOne(select):
    audio = random.choice(voice[select])
    # Проигрывание аудиофайла
    playsound.playsound(audio, True)

# Вторичный синтез
def synthesisTwo(text):
    audio = client.generate(
        text=text,
        voice=Voice(
            voice_id='CyvhG5XCUhl0VdMRKnDN'
        ),
        model="eleven_multilingual_v2",
    )
    play(audio)


# Главная функция
async def main():
    while True:
        result = await connect(type="passive")

        if "synthesis" in result["recipient"]:
            if result["content"][1] == "0":
                synthesisOne(int(result["content"][0]))
            elif result["content"][1] == "1":
                synthesisTwo(result["content"][0])

asyncio.run(main())