import os
import subprocess
import winreg
import shutil

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