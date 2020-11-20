get-childitem -path "." -recurse -filter "cr.bat" | foreach-object {
 Write-Output $_.Directory
 Set-Location $_.Directory
 Remove-Item -Path my_game.dist -Force -Recurse
 Remove-Item -Path "JMSS Science Fair Game" -Force -Recurse
 Start-Process -FilePath "C:\Program Files (x86)\Python38-32\python.exe" -ArgumentList ("-m nuitka --standalone --windows-dependency-tool=pefile my_game.py") -Wait -WorkingDirectory "." -NoNewWindow
 Rename-item -Path "my_game.dist" -NewName "JMSS Science Fair Game"
 Copy-Item -Path "resources\*" -Destination "JMSS Science Fair Game" -PassThru
 Copy-Item -Path "README.md" -Destination "JMSS Science Fair Game" -PassThru
 Start-Process -FilePath "C:\Program Files\7-Zip\7z.exe" -ArgumentList 'a JMSS-Science_Fair-Game.zip "JMSS Science Fair Game"' -Wait -NoNewWindow
 Set-Location ("..\")
}