import asyncio, sys, json

clients = []

# Получение сообщений и отправка
async def handle_client(reader, writer):
    clients.append(writer)

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            
            message = json.loads(data.decode())
            # Обработка завершения
            if (message["content"] == 'exit'):
                sys.exit()
            
            addr = writer.get_extra_info('peername')
            print(f"Connect: {addr}")

            # Отправляем сообщение всем клиентам, кроме отправителя
            for client in clients:
                if client != writer:
                    client.write(json.dumps(message).encode())
                    await client.drain()
    except ConnectionResetError:
        print(f"Disconnect (Error): {addr}")

    clients.remove(writer)
    writer.close()
    print(f"Disconnect: {addr}")

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 3150)

    async with server:
        await server.serve_forever()

asyncio.run(main())