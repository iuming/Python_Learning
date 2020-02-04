#BatchInstall.py
import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "beatifulsoup4", "wheel", "networkx", "sympy", "pyinstaller", "flask", "werobot", "pyqt5", "pandas", "pyopengl", "django", "pypdf2", "docopt", "pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")