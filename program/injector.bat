@echo off
setlocal enabledelayedexpansion

REM Get the directory and drive letter of this batch file
set "CURDIR=%~dp0"
set "MYDRIVE=%~d0"

REM Get the name of this batch file (without path)
set "MYNAME=%~nx0"

REM Set the Documents folder path
set "DOCS=%USERPROFILE%\Documents"

REM Loop through all .exe files in the current directory, except this script
for %%F in ("%CURDIR%*.exe") do (
    set "FNAME=%%~nxF"
    REM Only copy if not this batch file's EXE (if this is an EXE, skip it)
    if /I not "!FNAME!"=="%MYNAME:~0,-4%.exe" (
        if not "!FNAME!"=="%MYNAME%" (
            if not exist "%DOCS%\!FNAME!" (
                copy "%%F" "%DOCS%\!FNAME!"
                echo Copied !FNAME! to Documents.
            )
        )
    )
)

REM Eject the USB drive this script was run from (using PowerShell)
echo Ejecting USB drive %MYDRIVE% ...
powershell -Command "& { $drive = Get-WmiObject -Class Win32_Volume | Where-Object { $_.DriveLetter -eq '%MYDRIVE%' }; if ($drive -and $drive.DriveType -eq 2) { $drive.Dismount($false, $false) | Out-Null; Write-Host 'Ejected.' } else { Write-Host 'Not a removable drive or already ejected.' } }"
