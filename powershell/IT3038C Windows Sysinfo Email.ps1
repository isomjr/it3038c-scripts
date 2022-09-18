$IP = (Get-NetIPAddress).IPv4Address | Select-String "192*"
$DATE = Get-Date
$BODY = "This machine's IP is " + $IP + ". User is " + $env:USERNAME + ". Hostname is " + $env:USERDOMAIN + ". Powershell Version " + $Host.Version.Major + ". Today's date is " + $DATE.DateTime + "."

Send-MailMessage -To "reedws@ucmail.uc.edu" -From "isomjr@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)