import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from uart_protocol import UART_SCAN, UART_SETTING

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
        self.UI_UART_PORT_REFRESH()
        self.UI_UART()

    def UI_UART_FRAME(self):
        self.uart_frame = ttk.LabelFrame(self.root, text='UART CONNECTION')               
    
    def UI_UART_COM_CONFIG(self):
        self.uart_com_port = ttk.Label(self.uart_frame, text = 'Available Port (s)',width=15)
        self.COM_LIST = ["-----"]
        self.COM = tk.StringVar(self.root)
        self.COM.set(self.COM_LIST[0])
        self.COM_choices = ttk.OptionMenu(self.uart_frame,self.COM,*self.COM_LIST,command = self.uart_info)
    
    def UI_UART_BAUD_CONFIG(self):
        self.uart_com_rate = ttk.Label(self.uart_frame, text = 'Baud Rate',width=15)
        self.BAUD_LIST = ["-----","9600","19200","38400","57600","115200","460800","921600"]
        self.baud = tk.StringVar(self.root)
        self.baud.set(self.BAUD_LIST[7])
        self.baud_choices = ttk.OptionMenu(self.uart_frame,self.baud,*self.BAUD_LIST,command = self.uart_info)

    def UI_UART_CONNECT(self):
        self.connect = ttk.Button(self.uart_frame,text = 'Connect',command=self.uart_connection_callback, state = "disabled")
    
    def UI_UART_DISCONNECT(self):
        self.disconnect = ttk.Button(self.uart_frame,text = 'Disconnect',command=self.uart_disconnect_callback, state = "disabled")
    
    def UI_UART_PORT_REFRESH(self):
        self.refresh = ttk.Button(self.uart_frame,text="Refresh COM", command=self.uart_port_search)

    def UI_UART(self):
        self.uart_frame.grid(column = 0, row=0, padx=50, pady=30)
        self.uart_com_port.grid(column = 0, row = 1, ipadx=8, ipady= 0)
        self.uart_com_rate.grid(column = 0, row = 0, ipadx=8, ipady= 0)
        self.baud_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)
        self.COM_choices.grid(column=1,row=1,ipadx=10, ipady= 0)
        self.connect.grid(column=2,row=0,ipadx=10, ipady= 0)
        self.disconnect.grid(column=3,row=0,ipadx=10, ipady= 0)
        self.refresh.grid(column = 2,row=1,ipadx=10, ipady=0)
    
    def uart_connection_callback(self):
        stm32_connect = None
        PORT = self.COM.get()
        BAUD = self.baud.get()
        print(PORT, "",BAUD)
        self.STM32_UART = UART_SETTING(PORT,BAUD,'NONE',1,8,0.1,stm32_connect)
        self.STM32_UART.uartOpen()
        print(self.STM32_UART.uartStatus())
        if self.STM32_UART.uartStatus() is True:
            self.disconnect["state"] = "active"
            ConnMsg = f"Successfully Connected !"
            messagebox.showinfo("UART",ConnMsg)

   
    def uart_disconnect_callback(self):
        self.STM32_UART.uartClose()
        print('Disconnected !')
        print(self.STM32_UART.uartStatus())
        if self.STM32_UART.uartStatus() is False:
            self.disconnect["state"] = "disable"
            DisMsg = f"Disconnected !"
            messagebox.showinfo("UART", DisMsg)
    
    def uart_info(self,fuck):
        if "-----" in self.baud.get() or "-----"in self.COM.get():
            self.connect["state"]="disable"
            self.disconnect["state"] = "disable"
        elif "-----" not in self.baud.get() and "-----" not in self.COM.get():
            self.connect["state"] = "active"
    
    def uart_port_search(self):
        print('Refresh!')
        self.com_config = UART_SCAN()
        self.COM_LIST.clear()
        self.COM_LIST = self.com_config.com_scan(self.COM_LIST)
        self.COM = tk.StringVar(self.root)
        self.COM_choices = ttk.OptionMenu(self.uart_frame,self.COM,*self.COM_LIST,command=self.uart_info)
        self.COM_choices.grid(column=1,row=1,ipadx=10,ipady=0)