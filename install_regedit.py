import winreg
import os
import sys

from PyQt4 import QtGui
from ui.py.setup import Ui_setup

# C:/Users/Aydin/Desktop/quickConvert-master/Setup/Window
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


REG_PATH = r"AllFilesystemObjects\shell\Convert\command"
REG_PATH_ICON = r"AllFilesystemObjects\shell\Convert"


ICON_PATH = r"T:\DEV\generic\quick-convert\Icon\convert.ico"
RUN_PATH = r"T:\DEV\generic\quick-convert\Run\quickConvert.exe"


# SHELL_PATH = r"cmd.exe /K python {0}\\shell.py --path=%1".format(MAIN_PATH)
SHELL_PATH = r"cmd.exe /K {0} --path=%1".format(RUN_PATH)


class Setup(QtGui.QMainWindow, Ui_setup):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.arg = {}
        self.ui = Ui_setup()
        self.ui.setupUi(self)

        #override UI
        self.__run_path = RUN_PATH
        self.__icon_Path = ICON_PATH

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(sys.exit)

        self.ui.run_path_edit.setText(self.__run_path)
        self.ui.icon_path_edit.setText(self.__icon_Path)


    def ok(self):
        try:
            # ui get the edit lines
            self.__run_path = str(self.ui.run_path_edit.text())
            self.__icon_Path = str(self.ui.icon_path_edit.text())

            winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,REG_PATH)
            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, winreg.KEY_ALL_ACCESS)
            registry_key_icon = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH_ICON, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(registry_key_icon, r'Icon', 0, winreg.REG_SZ, self.__icon_Path)

            winreg.SetValueEx(registry_key, r'', 0, winreg.REG_SZ, self.generate_run_shell())
            winreg.CloseKey(registry_key)

        except Exception as e:
            QtGui.QMessageBox().information(QtGui.QWidget.__init__(self, None), "Access", str(e))
            return False
        QtGui.QMessageBox().information(QtGui.QWidget.__init__(self, None), "Success", "quickConvert has been added successfully in right click contextmenu file")


    def generate_run_shell(self):
        return r"cmd.exe /K {0} --path=%1".format(self.__run_path)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    setup1 = Setup()
    setup1.show()
    sys.exit(app.exec_())


