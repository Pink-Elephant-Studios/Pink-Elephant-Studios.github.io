cls
@echo off
:start

echo This is an example of a batch file.
set /p ans= "Do you understand? [y]es or [n]o?"

echo you answered %ans%

if %ans%==y GOTO yes
if %ans%==n GOTO no

:yes

echo Cool!
GOTO end
:no

echo well, then
GOTO start

:end
goto:eof