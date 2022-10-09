# GOAL: to check the space remaining of a selected drive.
# how to use: input a drive prompted to you
# made by Josh Isom


#populating variable with array object of valid drives
$DRIVELIST = Get-Volume | Select-Object DriveLetter | Where-Object DriveLetter -NotLike ''

#printing user prompt
Write-Host "Pick a drive to check the remaining disk space."
$DRIVELIST | foreach-object { Write-Host $_.DriveLetter }

#getting user input
$Selection = Read-Host

#function to check drive space
function Get-DriveSpace {

    param ( $Drive

    )
#check to see if drive selection is valid
if ($DRIVELIST.DriveLetter -contains $Drive){

#populate variable with raw bytes remaining in selected drive
$space = Get-Volume | Where-Object DriveLetter -eq $Drive | Select SizeRemaining | ForEach-Object {$_.SizeRemaining}

#formatting for GB, MB, KB, and B. no support for TB.
if ($space -gt 1GB) {
$space = $space / 1GB
Write-Host "$space GB"
} elseif ($space -gt 1MB) {
$space = $space / 1MB
Write-Host "$space MB"
} elseif ($space -gt 1KB) {
$space = $space / 1KB
Write-Host "$space KB"
} else {
Write-Host "$space B"
}


} #prompt for resubmitting selection after invalid input
else {
Write-Host "`n"
Write-Host "Invalid selection. Try again."
$DRIVELIST | foreach-object { Write-Host $_.DriveLetter }
$Selection = Read-Host
Get-DriveSpace $Selection

}

}

#this is where the magic happens
Get-DriveSpace $Selection