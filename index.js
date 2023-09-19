const { app } = require("electron");
const createWindow = require('./scripts/app');

app.whenReady().then(() => {createWindow()})