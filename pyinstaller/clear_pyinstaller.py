import shutil
import os

try:
    os.remove("quickConvert.spec")
    shutil.rmtree("build")
    shutil.rmtree("dist")
except FileNotFoundError as e:
    print("Already deleted")
