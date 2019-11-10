import winreg
from tkinter import messagebox
import os

# C:/Users/Aydin/Desktop/quickConvert-master/Setup/Window
current_path = os.path.dirname(os.path.realpath(__file__))

# C:\Users\Aydin\Desktop\quickConvert-master
MAIN_PATH = os.path.abspath(os.path.join(current_path, "..", ".."))

REG_PATH = r"AllFilesystemObjects\shell\Convert\command"
REG_PATH_ICON = r"AllFilesystemObjects\shell\Convert"

ICON_PATH = r"{0}\\Setup\\Icon\\convert.ico".format(MAIN_PATH)
SHELL_PATH = r"cmd.exe /K python {0}\\shell.py --path=%1".format(MAIN_PATH)

try:
    registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, winreg.KEY_ALL_ACCESS)
    registry_key_icon = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH_ICON, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(registry_key_icon, r'Icon', 0, winreg.REG_SZ, ICON_PATH)

    winreg.SetValueEx(registry_key, r'', 0, winreg.REG_SZ, SHELL_PATH)
    winreg.CloseKey(registry_key)

except PermissionError as e:
    messagebox.showinfo("Access", e)
    # print(e)





