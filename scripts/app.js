const { app, BrowserWindow, Tray, Menu, nativeImage } = require("electron");

const createWindow = () => {
    let win = new BrowserWindow({
        height: 600,
        width: 900,
        minHeight: 500,
        minWidth: 700,
        icon: "./style/img/Logo.png"
    });

    win.loadFile("index.html");
    // win.webContents.openDevTools();
}

module.exports = createWindow;