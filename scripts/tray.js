const { app, Tray, Menu, nativeImage, BrowserWindow } = require("electron");
const createWindow = require('./app');
const connect = require('./client');

const AllExit = () => {
    async function main() {
        console.log(await connect({ message: 'all%_GUI%_exit' }));
    };

    main().catch(err => {
        console.error(err);
    });

    app.quit()
    process.exit(1);
}

const startApps = () => {
    app.whenReady().then(() => {
        const icon = nativeImage.createFromPath('./style/img/Logo.png')
        let tray = new Tray(icon)

        const contextMenu = Menu.buildFromTemplate([
            { label: 'Exit', click: () => {AllExit()} },
        ])
        tray.setContextMenu(contextMenu)

        tray.setToolTip('Aurora')
        tray.setTitle('Aurora')
        tray.on('click', () => {
            BrowserWindow.getAllWindows().shift().show();
        });
        createWindow();
    })
}

module.exports = startApps;