$IP = (Get-NetIPAddress).IPv4Address | Select-String "192*"
$DATE = Get-Date
$BODY = "This machine's IP is " + $IP + ". User is " + $env:USERNAME + ". Hostname is " + $env:USERDOMAIN + ". Powershell Version " + $Host.Version.Major + ". Today's date is " + $DATE.DateTime + "."
Write-Host $BODY