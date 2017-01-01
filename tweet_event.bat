@echo off
:loop
ping 1.2.3.4 -n 1 -w 1000 > nul
set target=www.google.com
ping %target% -n 1 | find "TTL="
if errorlevel==1 goto ping

chdir /d %cd%
python googleCalendarAPI_quickstart.py
timeout /t 3 > nul
python TweetBot.py
timeout /t 3600 > nul
goto loop
