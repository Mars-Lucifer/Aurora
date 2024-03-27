import asyncio, sys, json

async def connect(recipient = None, sender = None, content = None, type = "active"):
    try:
        reader, writer = await asyncio.open_connection('localhost', 3150)

        try:
            # Формирование JSON сообщения
            message = {
                "recipient": recipient,
                "sender": sender,
                "content": content
            }
            message = json.dumps(message)

            # Отправляем сообщение
            if (type == "active"):
                writer.write(message.encode())
                await writer.drain()

            # Ждем ответа
            data = await reader.read(100)
            data = json.loads(data.decode())
            answer = {
                "recipient": data["sender"],
                "sender": data["recipient"],
                "content": "answer"
            }
            answer = json.dumps(answer)
        
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