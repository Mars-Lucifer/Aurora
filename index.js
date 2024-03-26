const startApps = require('./scripts/tray');
const connect = require('./scripts/client');

// Включаем звук
async function start() {
    console.log(await connect({ message: 'synthesis%_GUI%_2%_0' }));
};
start().catch(err => {
    console.error(err);
});

// Запускаем приложение
startApps();