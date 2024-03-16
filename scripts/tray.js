const { app, Tray, Menu, nativeImage } = require("electron");
const createWindow = require('./app');

const startApps = () => {
    app.whenReady().then(() => {
        const icon = nativeImage.createFromPath('./style/img/Logo.png')
        let tray = new Tray(icon)

        const contextMenu = Menu.buildFromTemplate([
            { label: 'Exit', click: () => {app.quit()} },
        ])
        tray.setContextMenu(contextMenu)

        tray.setToolTip('Aurora')
        tray.setTitle('Aurora')
        createWindow();
    })
}

module.exports = startApps;