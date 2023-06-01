import tkinter as tk
from tkinter import ttk

class UI_INIT:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('STM32 Motor Control Console')
        self.root.geometry("1500x700")
        self.root.resizable(False,False)
        self.root.iconbitmap(bitmap = 'motor.ico')

class UI_UART_CTL:
    def __init__(self,root):
        self.root = root
        self.UI_UART_FRAME()
        self.UI_UART_COM_CONFIG()
        self.UI_UART_BAUD_CONFIG()
        self.UI_UART_CONNECT()
        self.UI_UART_DISCONNECT()
        self.UI_UART()

    def UI_UART_FRAME(self):
        self.uart_frame = ttk.LabelFrame(self.root, text='UART CONNECTION')               
    
    def UI_UART_COM_CONFIG(self):
        self.uart_com_port = ttk.Label(self.uart_frame, text = 'Available Port (s)',width=15)
        self.COM_LIST = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10"]
        self.COM = tk.StringVar(self.root)
        self.COM.set(self.COM_LIST[9])
        self.COM_choices = ttk.OptionMenu(self.uart_frame,self.COM,*self.COM_LIST)
    
    def UI_UART_BAUD_CONFIG(self):
        self.uart_com_rate = ttk.Label(self.uart_frame, text = 'Baud Rate',width=15)
        self.BAUD_LIST = ["9600", "19200", "38400", "57600", "115200", "460800", "921600"]
        self.baud = tk.StringVar(self.root)
        self.baud.set(self.BAUD_LIST[4])
        self.baud_choices = ttk.OptionMenu(self.uart_frame,self.baud,*self.BAUD_LIST)

    def UI_UART_CONNECT(self):
        self.connect = ttk.Button(self.uart_frame,text = 'Connect',command=self.uart_connection_callback)
    
    def UI_UART_DISCONNECT(self):
        self.disconnect = ttk.Button(self.uart_frame,text = 'Disconnect',command=self.uart_disconnect_callback)

    def UI_UART(self):
        self.uart_frame.grid(column = 0, row=0, padx=50, pady=30)
        self.uart_com_port.grid(column = 0, row = 1, ipadx=8, ipady= 0)
        self.uart_com_rate.grid(column = 0, row = 0, ipadx=8, ipady= 0)
        self.baud_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)
        self.COM_choices.grid(column=1,row=1,ipadx=10, ipady= 0)
        self.connect.grid(column=2,row=0,ipadx=10, ipady= 0)
        self.disconnect.grid(column=3,row=0,ipadx=10, ipady= 0)
    
    def uart_connection_callback(self):
        print('Connected !')
    
    def uart_disconnect_callback(self):
        print('Disconnected !')