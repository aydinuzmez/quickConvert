import PyInstaller.__main__
import os

package_name = "quickConvert"
main_path = os.path.abspath("..")

ffmpeg_path = os.path.join(main_path, "bin", "ffmpeg.exe")
ffprobe_path = os.path.join(main_path, "bin", "ffprobe.exe")

shell_path = os.path.join(os.path.abspath(".."), 'run_shell.py')

PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onefile',
    '--windowed',
    '--add-data=%s;bin' % ffmpeg_path,
    '--add-data=%s;bin' % ffprobe_path,
    # '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
    shell_path
])
