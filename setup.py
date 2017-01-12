import sys
import os
from cx_Freeze import setup, Executable
import numpy

includefiles_list = []
numpy_path = os.path.dirname(numpy.__file__)
includefiles_list.append(numpy_path)
print(numpy_path)
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ['os', 'sys', 'matplotlib', 'pyside', 'numpy', 'tkinter', ],
                     "include_files": includefiles_list, "optimize": 2}
# 'scipy.sparse.lin'
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="AGeo",
      version="0.1",
      description="Geotechnical computing system",
      options={"build_exe": build_exe_options},
      executables=[Executable("C:\AGeo\AGeo.py", base=base)])
# PyInstaller -y -F --distpath="." -p "C:\Program Files\Anaconda3\envs\snakes\Lib\site-packages\PySide" ageo.py
