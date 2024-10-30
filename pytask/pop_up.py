import keyboard
import tkinter as tk
from pathlib import Path
import ctypes

#   store some stuff for win api interaction
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event
alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002

class window() :
    def __init__(self):
        self.window = None
        self.user_input = None
        self.user_end = False
        self.user_start = False
        keyboard.add_hotkey('win+alt+n', self.user_press_magic_combinaison)

    def user_press_magic_combinaison(self) :
        self.user_start = True

    def start(self):
        if self.window is not None :
            self.steal_focus()
            self.user_start = False
            return
        self.window = tk.Tk()
        self.window.geometry("275x75")
        self.window.wm_attributes('-toolwindow', 'True')
        self.window.wm_attributes('-topmost','True')
        self.window.bind('<Return>',self.user_push_enter)
        self.window.title("Quick Note ToDo")
        self.user_input = tk.StringVar()
        entry = tk.Entry(self.window, textvariable=self.user_input)
        entry.pack(fill='both')
        entry.focus()
        self.window.after(500,self.steal_focus) 
        self.user_start = False

    def stop(self) -> None:
        value_ret = self.user_input.get()
        self.window.destroy()
        self.window = None
        self.user_input = None
        self.user_end = False
        return value_ret
    
    def update(self) :
        if self.window is not None :
            self.window.update()

    def steal_focus(self):
        keybd_event(alt_key, 0, extended_key | 0, 0)
        set_to_foreground(self.window.winfo_id())
        keybd_event(alt_key, 0, extended_key | key_up, 0)

    def user_push_enter(self,event):
        self.user_end = True