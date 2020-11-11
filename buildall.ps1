get-childitem -path "." -recurse -filter "cr.bat" | foreach-object {
 Set-Location $_.Directory
 start-process $ENV:SystemRoot\system32\cmd.exe -argumentlist ('/c "' + $_.FullName + '"')
}

