Write-Host "Welcome to the Tasklist"
Write-Host "What is your username?"
$name = Read-Host
$filepath = $name + "tasklist.txt"

if (Test-Path $filepath) {
    $oldtasklist = Get-Content $filepath
}
else {
    Write-Host "Welcome, new user!"
    New-Item -Path $filepath -ItemType File
}
