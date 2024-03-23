const net = require('net');

async function connect(message = false) {
    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150, host: '127.0.0.1' }, () => {

            if (message) {
                client.write(message);
            }

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
    await connect(`Hello. This client 1`);
};

main().catch(err => {
    console.error(err);
});

module.exports = connect;