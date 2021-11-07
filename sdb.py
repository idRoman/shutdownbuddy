from tkinter import *
from datetime import datetime, timedelta
import os
import sys

program = Tk()
program.title("ShutDownBuddy 1.0")
program.resizable(0, 0)
#space = Canvas(program, width=250, height=250)
program.geometry("230x200")
program.rowconfigure(4, weight=1)
program.columnconfigure(5, weight=1)
#space.rowconfigure(4, weight=20, minsize=20)
#space.columnconfigure(6, weight=20, minsize=20)
#space.grid(columnspan=6, rowspan=4)

def file_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

program.iconbitmap(file_path('off_btn.ico'))

def info_text(msg):
    time_text.config(text=msg)

def button_start():
    try:
        calculation = int(time_value.get())*60
        if int(calculation) > 0:
            command = "shutdown -s -t " + str(calculation)
            os.system(command)
            new_time = datetime.now() + timedelta(minutes=calculation/60)
            info_text("ACTIVE: Shutdown @: " + new_time.strftime("%H:%M:%S"))
            program.iconbitmap(file_path('on_btn.ico'))
        else:
            info_text("ERROR: Value can't be 0")
    except ValueError:
        info_text("ERROR: Enter only numbers")

def button_stop():
    os.system("shutdown -a")
    info_text("NOT ACTIVE: Stopped")
    program.iconbitmap(file_path('off_btn.ico'))

time_text = Label(program, font="Raleway", text="")
time_text.grid(row=0, column=2, columnspan=3, pady=5)
shutdown_text = Label(program, font="Raleway", text="Shutdown in:")
shutdown_text.grid(row=1, column=2, sticky=EW)
time_value = Entry(program, width=5, font="Raleway", justify=CENTER)
time_value.grid(row=1, column=3, sticky=EW, pady=5)
time_value.insert(0, "30")
minutes_text = Label(program, font="Raleway", text="Minutes")
minutes_text.grid(row=1, column=4, sticky=EW)
start = Button(program, text="Start", font="Raleway", width=20, height=2, command=button_start)
start.grid(row=2, column=2, columnspan=3, sticky=EW, padx=10, pady=5)
stop = Button(program, text="Stop", font="Raleway", width=20, height=2, command=button_stop)
stop.grid(row=3, column=2, columnspan=3, sticky=EW, padx=10)

program.mainloop()