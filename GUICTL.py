import tkinter as tk
from tkinter import ttk

class GUIConsole:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('STM32 Motor Control Console')
        self.root.geometry("1500x700")
        self.root.resizable(False,False)
        self.root.iconbitmap(bitmap = 'motor.ico')

class GUIConfig:
    def __init__(self,root):
        self.root = root
        self.uart_config()
        self.put_uart_features()

    def uart_config(self):
        self.uart_frame = ttk.LabelFrame(self.root, text='UART CONNECTION')
        self.uart_com_port = ttk.Label(self.uart_frame, text = 'Available Port (s)',width=15)
        self.uart_com_rate = ttk.Label(self.uart_frame, text = 'Baud Rate',width=15)
        BAUD_LIST = ["9600", "19200", "38400", "57600", "115200", "460800", "921600"]
        self.baud = tk.StringVar(self.root)
        self.baud.set(BAUD_LIST[4])
        self.baud_choices = ttk.OptionMenu(self.uart_frame,self.baud,*BAUD_LIST)
        self.COM_LIST = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10"]
        self.COM = tk.StringVar(self.root)
        self.COM.set(self.COM_LIST[9])
        self.COM_choices = ttk.OptionMenu(self.uart_frame,self.COM,*self.COM_LIST)
        self.connect = ttk.Button(self.uart_frame,text = 'Connect')
        self.disconnect = ttk.Button(self.uart_frame,text = 'Disconnect')

    def put_uart_features(self):
        self.uart_frame.grid(column = 0, row=0, padx=50, pady=30)
        self.uart_com_port.grid(column = 0, row = 1, ipadx=8, ipady= 0)
        self.uart_com_rate.grid(column = 0, row = 0, ipadx=8, ipady= 0)
        self.baud_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)
        self.COM_choices.grid(column=1,row=1,ipadx=10, ipady= 0)
        self.connect.grid(column=2,row=0,ipadx=10, ipady= 0)
        self.disconnect.grid(column=3,row=0,ipadx=10, ipady= 0)

