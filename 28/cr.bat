del my_game.7z
del my_game.zip

call .\build.bat
..\7zr a my_game.7z ..\7zr.exe -mx -mf=BCJ2
copy /b ..\7zSD.sfx + config.txt + my_game.7z my_game.zip