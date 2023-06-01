# This is an automated data logging system of STM32 Motor Controller
# Users can make use of STM32 Motor Control Protocol to retrieve the motors' parameters & status to work on the evalution
# For more details, users are required to read the STM32MCP SDK Datasheet
# This software is compible to Windows, MacOS and Linux Platform
# For the hardware implementation's purpose, users are suggested to use MacOS or Linux Platform
# During dyno's testing, it is encouraged to implement this Real Time software into the Raspberry Pi! 
# It is used for testing for the motor's power efficienct Pout/Pin
# It could be used to simulate the dashboard's environment for debugging purpose
# For the advanced data analysis, it might be required to upload the logged data to Google Drive
# For more information, please go to https://developers.google.com/drive/api/quickstart/python
# Reference : https://www.youtube.com/watch?v=u3NnzRIwjH8&list=PLtVUYRe-Z-meHdTlzqCHGPjZvnL2VZVn8&index=2
#             https://www.pythontutorial.net/tkinter/

import matplotlib
import serial
import tkinter as tk
from tkinter import ttk
from GUICTL import GUIConsole,GUIConfig
''''
root = tk.Tk()
root.title('STM32 Motor Control Console')
root.geometry("1500x700")
root.resizable(False,False)
root.iconbitmap(bitmap = 'motor.ico')

#Create the Frame
uart_frame = ttk.LabelFrame(root, text='UART CONNECTION')
uart_frame.grid(column = 0, row=0, padx=50, pady=30)

#PUT THEM ON THE FRAME
uart_com_port = ttk.Label(uart_frame, text = 'Available Port (s)',width=15)
uart_com_port.grid(column = 0, row = 1, ipadx=8, ipady= 0)


uart_com_rate = ttk.Label(uart_frame, text = 'Baud Rate',width=15)
uart_com_rate.grid(column = 0, row = 0, ipadx=8, ipady= 0)

BAUD_LIST = ["9600", "19200", "38400", "57600", "115200", "460800", "921600"]
baud = tk.StringVar(root)
baud.set(BAUD_LIST[4])
baud_choices = ttk.OptionMenu(uart_frame,baud,*BAUD_LIST)
baud_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)

COM_LIST = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10"]
COM = tk.StringVar(root)
COM.set(COM_LIST[9])
COM_choices = ttk.OptionMenu(uart_frame,COM,*COM_LIST)
COM_choices.grid(column=1,row=1,ipadx=10, ipady= 0)

connect = ttk.Button(uart_frame,text = 'Connect')
connect.grid(column=2,row=0,ipadx=10, ipady= 0)

disconnect = ttk.Button(uart_frame,text = 'Disconnect')
disconnect.grid(column=3,row=0,ipadx=10, ipady= 0)
'''
stm32MCP = GUIConsole()
stm32Config = GUIConfig(stm32MCP.root)
stm32MCP.root.mainloop()