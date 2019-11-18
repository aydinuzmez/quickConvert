import shutil
import os

try:
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.remove("quickConvert.spec")
except WindowsError as e:
    print("{0} already has been deleted".format(e.filename))


try:
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.remove("install_regedit.spec")

except WindowsError as e:
    print("{0} already has been deleted".format(e.filename))

