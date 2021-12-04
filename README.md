__author__ = "Roman Guttmann"

__license__ = "Open-Source license"

__version__ = "1.1"

__maintainer__ = "Roman Guttmann"

__email__ = "github@zupo.sk"

Creating EXE from python file using Pyinstaller.

Installing pyinstaller on Windows:
- open CMD
- write and execute: "pip install pyinstaller"

Creating EXE:
- open CMD in shutdownbuddy folder
- write and execute: "pyinstaller --onefile --windowed --icon=off_btn.ico --add-data "off_btn.ico;." --add-data "on_btn.ico;." sdb.py"
- .exe file should be located in dist folder

FREE TO USE/EDIT - Open Source Lincense
