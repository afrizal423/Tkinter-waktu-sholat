import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("sholatapp.py", base=base, icon="masjid.ico")]

cx_Freeze.setup(
    name = "JadwalSholat",
    options = {"build_exe": {"packages":["tkinter"], "include_files":["masjid.ico"]}},
    version = "0.01",
    description = "Afrizal",
    executables = executables
    )