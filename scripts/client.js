const net = require('net');

async function connect(options) {
    const { message = NaN, type = "active" } = options;

    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150, host: '127.0.0.1' }, () => {

            if (type == "active") {
                client.write(message);
            };

            client.on('data', data => {
                if (type == "passive") {
                    client.write("ok");
                };

                client.end();
                return resolve(data.toString().split("%_"));
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