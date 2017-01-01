:ping
ping 1.2.3.4 -n 1 -w 1000 > null
set target=www.google.com
ping %target% -n 1 | find "TTL="
if errorlevel==1 goto ping
chdir /d %cd%
python googleCalendarAPI_quickstart.py