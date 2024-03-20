import asyncio

clients = []

# Получение сообщений и отправка
async def handle_client(reader, writer):
    clients.append(writer)

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            
            message = data.decode()
            addr = writer.get_extra_info('peername')
            print(f"Connect: {addr}")

            # Отправляем сообщение всем клиентам, кроме отправителя
            for client in clients:
                if client != writer:
                    client.write(f"{addr[0]}:{addr[1]}: {message}".encode())
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