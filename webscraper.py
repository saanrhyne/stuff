Write-Host "Enter the Link:"
$link = Read-Host
$page = Invoke-WebRequest -uri $link
$page -match "<p>.*?</p>"
foreach ($match in $matches) {
  Write-Host $match
}
