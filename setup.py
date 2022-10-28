from cx_Freeze import setup, Executable

base = None    

executables = [Executable("AutomatedDataEntry.py", target_name = "Automated Data Entry.exe", base=base)]

packages = ["idna", "numpy", "cv2", "tkinter", "PIL", "pytesseract", "pickle", "os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Automated Data Entry",
    options = options,
    version = "1.3.1",
    description = '',
    executables = executables
)
