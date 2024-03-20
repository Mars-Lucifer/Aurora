const net = require('net');

async function connect(message) {
    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150, host: '127.0.0.1' }, () => {

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

module.exports = connect;