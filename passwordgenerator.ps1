Write-Host "Warning: This script will change the password of the user you input." -ForegroundColor Red
Write-Host "Enter the username:"
$user = Read-Host
$chars = @("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "1","2","3","4","5","6","7","8","9","0",
           "!","@","#","`$","%","^","&","*","(",")","_","-","+","{","}","[","]","|","<",">","?","=","~","\","/",",",".")
$password = $chars | Get-Random -Count 18 | Join-String
Get-LocalUser -Name "$user"
Set-LocalUser -Password "$password"
Write-Output "$user's New Password: $password"
