import PyInstaller.__main__
import os

package_name = "install_regedit"
main_path = os.path.abspath("..")



shell_path = os.path.join(os.path.abspath(".."), 'install_regedit.py')

PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onefile',
    '--windowed',
    # '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
    shell_path
])
