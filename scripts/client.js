const net = require('net');

async function connect(options) {
    const { message = NaN, type = "active" } = options;

    return new Promise((resolve, reject) => {
        const client = net.createConnection({ port: 3150, host: '127.0.0.1' }, () => {

            if (type == "active") {
                client.write(JSON.stringify(message));
            };

            client.on('data', data => {
                data = JSON.parse(data.toString());
                if (type == "passive") {
                    const answer = {
                        recipient: data.sender,
                        sender: data.recipient,
                        content: "answer"
                    };
                    client.write(JSON.stringify(answer));
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