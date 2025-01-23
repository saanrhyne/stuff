# Script to search for a specific reg key
Write-Host "What reg key to seach for?"
$reg = Read-Host

Get-ChildItem -Path 'Registry::HKEY_LOCAL_MACHINE\SOFTWARE' -Recurse | Where-Object { $_.PSChildName -match $reg } 
