@echo off
cd scripts
start /B python server.py
timeout 2
start /B python synthesis.py
timeout 2
start /B npm start