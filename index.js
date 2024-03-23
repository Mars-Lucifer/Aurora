const startApps = require('./scripts/tray');
const connect = require('./scripts/client');

async function main() {
    await connect(`Hello. This client 1`);
};

main().catch(err => {
    console.error(err);
});

startApps();