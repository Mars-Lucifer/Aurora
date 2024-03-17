import asyncio

async def connect(message):
    reader, writer = await asyncio.open_connection('localhost', 3150)

    try:
        # Отправляем сообщение на сервер
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
    # Пример использования
    i = 0
    while True:
        i+=1
        await connect(f"Hello cl2 - x{i}")

asyncio.run(main())