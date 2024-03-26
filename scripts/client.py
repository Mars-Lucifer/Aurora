import asyncio, sys

async def connect(message = None, type = "active"):
    try:
        reader, writer = await asyncio.open_connection('localhost', 3150)

        try:
            # Отправляем сообщение
            if (type == "active"):
                writer.write(message.encode())
                await writer.drain()

            # Ждем ответа
            data = await reader.read(100)
            data = data.decode().lower().split("%_")
            print(data)

            answer = f'{data[1]}%_{data[0]}%_answer'
        
            # Отправляем ответ
            if (type == "passive"):
                writer.write(answer.encode())
                await writer.drain()

            # Получаем данные
            return data
        finally:
            # Закрываем соединение
            writer.close()
            await writer.wait_closed()
    except:
        sys.exit()