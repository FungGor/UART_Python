import tkinter as tk
from tkinter import ttk

windows_width = 2000
windows_height = 500

class GUIConsole:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('STM32 Motor Control Console')
        self.root.geometry("1500x700")
        self.root.resizable(False,False)
        self.root.iconbitmap(bitmap = 'motor.ico')
