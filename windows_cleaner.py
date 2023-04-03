import os
import subprocess
import winreg
import shutil
import urllib.request
import zipfile
import wmi


# Set console window title
os.system("title Windows_Optimisation_Pack Cleaner | /u00A9 unofficialdxnny")

# Delete all shadow copies
subprocess.run(["vssadmin", "delete", "shadows", "/all", "/quiet"], stdout=subprocess.DEVNULL)

# Create system restore point
os.system("Checkpoint-Computer -Description 'Windows_Optimisation_Pack Cleaner' -RestorePointType MODIFY_SETTINGS")

# Modify registry keys to clean up disk space
with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/VolumeCaches") as key:
    for i in range(winreg.QueryInfoKey(key)[0]):
        subkey_name = winreg.EnumKey(key, i)
        if subkey_name == "DownloadsFolder":
            continue
        subkey_path = "SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/VolumeCaches//" + subkey_name
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_WRITE) as subkey:
            winreg.SetValueEx(subkey, "StateFlags0001", 0, winreg.REG_DWORD, 2)

# Flush DNS cache
os.system("ipconfig /flushdns")

# Run system file checker
os.system("sfc /SCANNOW")

# Analyze component store
os.system("Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore")

# Remove superseded updates
os.system("Dism.exe /Online /Cleanup-Image /spsuperseded")

# Start component cleanup
os.system("Dism.exe /online /Cleanup-Image /StartComponentCleanup")

# Clear browser cache
os.system("Clear-BCCache -Force -ErrorAction SilentlyContinue")

# Remove temporary files
for path in [os.environ['temp'], os.environ['windir'] + '\\Temp']:
    os.system(f"Get-ChildItem -Path {path} -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove prefetch files
os.system("Get-ChildItem -Path $env:windir\\Prefetch -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove software distribution files
os.system("Get-ChildItem -Path $env:SystemRoot\\SoftwareDistribution\\Download -Recurse -Force | Remove-Item -Recurse -Force")

# Remove retail demo files
os.system("Get-ChildItem -Path $env:ProgramData\\Microsoft\\Windows\\RetailDemo -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove AMD files
for path in [os.environ['LOCALAPPDATA'] + '\\AMD', os.environ['windir'] + '\\..\\AMD']:
    os.system(f"Get-ChildItem -Path {path} -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove NVIDIA files
for path in [os.environ['LOCALAPPDATA'] + '\\NVIDIA\\DXCache', os.environ['LOCALAPPDATA'] + '\\NVIDIA\\GLCache']:
    os.system(f"Get-ChildItem -Path {path} -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove Intel files
os.system("Get-ChildItem -Path $env:APPDATA\\..\\locallow\\Intel\\ShaderCache -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove crash dumps
os.system("Get-ChildItem -Path $env:LOCALAPPDATA\\CrashDumps -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove AMD files (2)
os.system("Get-ChildItem -Path $env:APPDATA\\..\\locallow\\AMD -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")

# Remove Microsoft Office cache
os.system("Get-ChildItem -Path $env:windir\\..\\MSOCache")

# Remove Call of Duty shader cache
os.system(f"Get-ChildItem -Path {os.environ['ProgramFiles(x86)']}\\Steam\\steamapps\\common\\\"Call of Duty HQ\"\\shadercache -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse")


def delete_folder(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass

def main():
    if winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\EscapeFromTarkov"):
        subprocess.call(["taskkill", "/F", "/IM", "EscapeFromTarkov.exe"])
        escape_from_tarkov = winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\EscapeFromTarkov", "InstallLocation")[0]
        delete_folder(os.path.join(escape_from_tarkov, "Logs"))
        delete_folder(os.path.join(os.environ["TEMP"], "Battlestate Games"))

    if winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 1938090"):
        subprocess.call(["taskkill", "/F", "/IM", "cod.exe"])
        call_of_duty_mw2_steam = winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 1938090", "InstallLocation")[0]
        delete_folder(os.path.join(call_of_duty_mw2_steam, "shadercache"))

    if winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Call of Duty"):
        subprocess.call(["taskkill", "/F", "/IM", "cod.exe"])
        call_of_duty_mw2_battlenet = winreg.QueryValueEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Call of Duty", "InstallLocation")[0]
        delete_folder(os.path.join(call_of_duty_mw2_battlenet, "shadercache"))

    subprocess.call(["lodctr", "/r"])
    subprocess.call(["lodctr", "/r"])
    os.system("cls")
    print("Datentraeger Bereinigung wird gestartet...")
    subprocess.call(["cleanmgr.exe", "/sagerun:1", "/d", "C:"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("The System has been cleaned")

if __name__ == "__main__":
    main()



hash = {}
ScriptFolder = os.path.join(os.environ['TEMP'], 'Windows_Optimisation_Pack')
try:
    winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Windows_Optimisation_Pack')
except:
    pass
WindowsVersion = wmi.WMI().Win32_OperatingSystem()[0].Caption
InstalledSoftware = [item.DisplayName for item in winreg.QueryInfoKey(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'))[0]]
if not os.path.exists(ScriptFolder):
    os.mkdir(ScriptFolder)


def WindowsTweaks_Services():
    subprocess.run(["Stop-Service", "WpcMonSvc"])
    subprocess.run(["Stop-Service", "SharedRealitySvc"])
    subprocess.run(["Stop-Service", "Fax"])
    subprocess.run(["Stop-Service", "autotimesvc"])
    subprocess.run(["Stop-Service", "wisvc"])
    subprocess.run(["Stop-Service", "SDRSVC"])
    subprocess.run(["Stop-Service", "MixedRealityOpenXRSvc"])
    subprocess.run(["Stop-Service", "WalletService"])
    subprocess.run(["Stop-Service", "SmsRouter"])
    subprocess.run(["Stop-Service", "SharedAccess"])
    subprocess.run(["Stop-Service", "MapsBroker"])
    subprocess.run(["Stop-Service", "PhoneSvc"])
    subprocess.run(["Stop-Service", "ScDeviceEnum"])
    subprocess.run(["Stop-Service", "icssvc"])
    subprocess.run(["Stop-Service", "edgeupdatem"])
    subprocess.run(["Stop-Service", "edgeupdate"])
    subprocess.run(["Stop-Service", "MicrosoftEdgeElevationService"])
    subprocess.run(["Stop-Service", "RetailDemo"])
    subprocess.run(["Stop-Service", "MessagingService"])
    subprocess.run(["Stop-Service", "PimIndexMaintenanceSvc"])
    subprocess.run(["Stop-Service", "OneSyncSvc"])
    subprocess.run(["Stop-Service", "UnistoreSvc"])
    subprocess.run(["Stop-Service", "DiagTrack"])
    subprocess.run(["Stop-Service", "dmwappushservice"])
    subprocess.run(["Stop-Service", "diagnosticshub.standardcollector.service"])
    subprocess.run(["Stop-Service", "diagsvc"])
    subprocess.run(["Stop-Service", "WerSvc"])
    subprocess.run(["Stop-Service", "wercplsupport"])
    subprocess.run(["Set-Service", "WpcMonSvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "SharedRealitySvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "Fax", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "autotimesvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "wisvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "SDRSVC", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "MixedRealityOpenXRSvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "WalletService", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "SmsRouter", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "SharedAccess", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "MapsBroker", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "PhoneSvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "ScDeviceEnum", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "TabletInputService", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "icssvc", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "edgeupdatem", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "edgeupdate", "-StartupType", "Disabled"])
    subprocess.run(["Set-Service", "MicrosoftEdgeElevationService", "-StartupType", "Disabled"])
    
services = [
    "RetailDemo",
    "MessagingService",
    "PimIndexMaintenanceSvc",
    "OneSyncSvc",
    "UnistoreSvc",
    "DiagTrack",
    "dmwappushservice",
    "diagnosticshub.standardcollector.service",
    "diagsvc",
    "WerSvc",
    "wercplsupport"
]

for service in services:
    subprocess.run(["sc", "config", service, "start=", "disabled"])



