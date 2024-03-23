import asyncio

async def connect(message=False):
    reader, writer = await asyncio.open_connection('localhost', 3150)

    try:
        # Отправляем сообщение на сервер
        if (message):
            writer.write(message.encode())
            await writer.drain()

        # Ждем ответа от сервера
        data = await reader.read(100)
        print(data.decode())
    finally:
        # Закрываем соединение
        writer.close()
        await writer.wait_closed()

async def main():
    await connect()

asyncio.run(main())