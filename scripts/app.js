const { app, BrowserWindow, Tray, Menu } = require("electron");

const createWindow = () => {
    const win = new BrowserWindow({
        height: 600,
        width: 900,
        minHeight: 500,
        minWidth: 700,
        icon: "./style/icons/Logo.ico"
    });

    tray = new Tray("./style/icons/Logo.ico");
    const contextMenu = Menu.buildFromTemplate([
        { label: "Aurora", type: 'normal', icon: './style/icons/Logo.ico' },
        { label: "Stop", type: 'normal' }
    ]);
    tray.setToolTip('My app.');
    tray.setContextMenu(contextMenu);

    win.loadFile("index.html");
    // win.webContents.openDevTools();
}

module.exports = createWindow;