del my_game.7z
del my_game.zip

call .\build.bat
..\7zr a -sfx my_game.zip dist
