import asyncio

async def connect(message = None, type = "active"):
    reader, writer = await asyncio.open_connection('localhost', 3150)

    try:
        # Отправляем сообщение
        if (type == "active"):
            writer.write(message.encode())
            await writer.drain()

        # Ждем ответа
        data = await reader.read(100)
    
        # Отправляем ответ
        if (type == "passive"):
            writer.write("ok".encode())
            await writer.drain()

        # Получаем данные
        return data.decode()
    finally:
        # Закрываем соединение
        writer.close()
        await writer.wait_closed()