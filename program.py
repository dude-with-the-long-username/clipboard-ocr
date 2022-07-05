import subprocess

command = 'xclip -selection clipboard -t image/png -o > test.png'  # outputs image in clipboard to test.png (if image exists in clipboard)
subprocess.call(command, shell=True)


