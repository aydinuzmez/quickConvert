import PyInstaller.__main__
import os

package_name = "quickConvert"
main_path = os.path.abspath("..")
ffmpeg_path = os.path.join(main_path, "lib", "ffmpeg.exe")
shell_path = os.path.join(os.path.abspath(".."), 'shell.py')

PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onefile',
    '--windowed',
    '--add-data=%s;ffmpeg' % ffmpeg_path,
    # '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
    shell_path,
])
