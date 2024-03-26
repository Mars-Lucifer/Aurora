const net = require('net');

async function connect(options) {
    const { message = NaN, type = "active" } = options;

    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150, host: '127.0.0.1' }, () => {

            if (type == "active") {
                client.write(message);
            };

            client.on('data', data => {
                data = data.toString().toLowerCase().split("%_")
                if (type == "passive") {
                    client.write(`${data[1]}%_${data[0]}%_answer`);
                };

                client.end();
                return resolve(data);
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