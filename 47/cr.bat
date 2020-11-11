del my_game.7z
del my_game.exe

call .\build.bat
..\7zr a -sfx my_game.exe dist
