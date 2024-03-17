const net = require('net');

async function connect(message) {
    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150 }, () => {

            client.write(message);

            client.on('data', data => {
                console.log(data.toString());
                client.end();
                resolve();
            });

            client.on('end', () => {});
        });

        client.on('error', err => {
            console.error('Error:', err);
            reject(err);
        });
    });
}

async function main() {
    // Пример использования
    let i = 0;
    while (true) {
        i++;
        await connect(`Hello cl2 - x${i}`);
    }
}

main().catch(err => {
    console.error(err);
});