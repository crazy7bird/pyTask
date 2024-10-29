import keyboard
import time
import tkinter as tk
from pathlib import Path
import ctypes
import os

start = False
stop = False
window = None
user_input = None


#   store some stuff for win api interaction
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event
alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002

def steal_focus(window:tk):
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(window.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

    entry.focus_set()

def startAwin():
    global start 
    start = True

def killAwin(event):
    global stop 
    stop = True

keyboard.add_hotkey('win+alt+n', startAwin)

class backlog() :
    def __init__(self, filePath : Path = ".note"):
        self.filePath = filePath
        self.taskList= []
        self.fileLoad()
        pass

    def fileLoad(self, filePath : Path = None) :
        if filePath is None :
            filePath = self.filePath
        with open(filePath, "rt") as file:
            for line in file.readlines() :
                task = line.rstrip('\n')
                if task :
                    self.taskList.append(task)

    def list_backlog(self) :
        return self.taskList

    def add_task(self, task:str) :
        self.taskList.append(task)
    
    def save_backlog(self) :
        with open(self.filePath, "wt") as f:
            for line in self.taskList:
                f.write(f"{line}\n")

class window():
    def __init__(self):
        self.window = None
        self.user_input = None
        pass
    def start(self):
        window = self.window
        if window is not None :
            return
        window = tk.Tk()
        window.geometry("275x75")
        window.wm_attributes('-toolwindow', 'True')
        window.wm_attributes('-topmost','True')
        window.bind('<Return>',killAwin)
        window.title("Quick Note ToDo")
        self.user_input = tk.StringVar()
        entry = tk.Entry(window, textvariable=user_input)
        entry.pack(fill='both')
        entry.focus()
        window.after(500,steal_focus,window) 
    def stop(self) -> None:
        value_ret = self.user_input.get()
        print(f"Final Entry : {value_ret}")
        window.destroy()
        self.window = None
        self.user_input = None
        return value_ret


b = backlog()
w = window()

t = time.time()
while True :
    if start and window is None:
        window = tk.Tk()
        window.geometry("275x75")
        window.wm_attributes('-toolwindow', 'True')
        window.wm_attributes('-topmost','True')
        window.bind('<Return>',killAwin)
        window.title("Quick Note ToDo")
        user_input = tk.StringVar()
        entry = tk.Entry(window, textvariable=user_input)
        entry.pack(fill='both')
        entry.focus()
        window.after(500,steal_focus,window)
        start = False
    
    if stop :
        print(f"Final Entry : {user_input.get()}")
        b.add_task(user_input.get())
        b.save_backlog()
        window.destroy()
        window = None
        user_input = None
        stop = False

    if window is not None :
        window.update()


    if time.time() > t + 4 :
        print(f"Entry : {b.list_backlog()}")
        t = time.time()