const startApps = require('./scripts/tray');
const connect = require('./scripts/client');

// Включаем звук
async function start() {
    await connect({ message: { recipient: "synthesis", sender: "GUI main", content: ["2", "0"] }, type: "active" });
};
start().catch(err => {
    console.error(err);
});

// Запускаем приложение
startApps();