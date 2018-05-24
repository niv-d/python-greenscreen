from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna","cv2","numpy","PyQt5"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Python Greenscreen",
    options = options,
    version = "0.1.0",
    description = 'Create greenscreen with any webcam',
    executables = executables
)