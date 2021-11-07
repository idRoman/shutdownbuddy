Creating EXE from python file using pyinstaller.

Installing pyinstaller on Windows:
- open CMD
- write and execute: pip install pyinstaller

Creating EXE:
- open CMD in shutdownbuddy folder
- write and execute: pyinstaller --onefile --windowed --add-data "off_btn.ico;." --add-data "on_btn.ico;." sdb.py
- .exe file should be located in dist folder


FREE TO USE/EDIT