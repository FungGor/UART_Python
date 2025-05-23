import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from uart_protocol import UART_SCAN, UART_SETTING
class UI_INIT:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('STM32 Motor Control Console')
        self.root.geometry("1700x700")
        self.root.resizable(True,True)
        self.root.iconbitmap(bitmap = 'motor.ico')

class UI_Motor_CTL_Mode:
    def __init__(self,root):
        self.root = root
        self.UI_Motor_Mode_Frame()
        self.UI_Motor_Mode_Config()
        self.UI_Motor_Speed_Frame()
        self.UI_Motor_Speed_Control_Config()
        self.UI_Motor_Speed_PID_Frame()
        self.UI_Motor_Speed_Control_PID_Config()
        self.UI_Motor_Torque_Frame()
        self.UI_Motor_Torque_Control_Config()
        self.UI_Motor_Torque_PID_Frame()
        self.UI_Motor_Torque_Control_PID_Config()
        self.UI_PUT_MOTOR_MODE_FRAME()

    def UI_Motor_Mode_Frame(self):
        self.mode_frame = ttk.LabelFrame(self.root, text='Motor Speed/Torque Control')
    
    def UI_Motor_Speed_Frame(self):
        self.speed_ctl_frame = ttk.LabelFrame(self.mode_frame, text = "Speed Control")
    
    def UI_Motor_Torque_Frame(self):
        self.torque_ctl_frame = ttk.LabelFrame(self.mode_frame, text = "Torque/Current Control")
    
    def UI_Motor_Speed_PID_Frame(self):
        self.speed_pid_frame = ttk.LabelFrame(self.mode_frame, text = "Speed Gains")
    
    def UI_Motor_Torque_PID_Frame(self):
        self.torque_pid_frame = ttk.LabelFrame(self.mode_frame, text = "Current Gains")
    
    def UI_Motor_Mode_Config(self):
        self.mode_choose = ttk.Label(self.mode_frame,text = 'Select Motor Control Mode :')
        self.MODE = ["Speed Mode","Torque Mode"]
        self.motor = tk.StringVar(self.root)
        self.motor.set(self.MODE)
        self.MOTOR_CHOICE = ttk.OptionMenu(self.mode_frame,self.motor,self.MODE[0],*self.MODE)
        self.CTL_OK = ttk.Button(self.mode_frame, text = "OK", command = self.mode_determine)
    
    def UI_Motor_Speed_Control_Config(self):
        self.Speed = ttk.Label(self.speed_ctl_frame, text = "Target Speed",state = "disabled")
        self.inputSpeed = tk.Text(self.speed_ctl_frame, height=1, width=5, bg = "light cyan", state = "disabled")
        self.duration = ttk.Label(self.speed_ctl_frame, text = "Durations",state = "disabled" )
        self.ramping  = tk.Text(self.speed_ctl_frame,height=1, width=5, bg = "light cyan", state = "disabled" )
        self.Exec = ttk.Button(self.speed_ctl_frame,text = "Execute Ramp", state = "disabled")
    
    def UI_Motor_Speed_Control_PID_Config(self):
        self.Speed_P = ttk.Label(self.speed_pid_frame, text = "Kp",state = "disabled")
        self.Speed_Kp = tk.Text(self.speed_pid_frame,height=1, width=5, bg = "light cyan",state = "disabled")
        self.Speed_I = ttk.Label(self.speed_pid_frame,text = "KI",state = "disabled") 
        self.Speed_KI =  tk.Text(self.speed_pid_frame,height=1, width=5, bg = "light cyan",state = "disabled")
    
    def UI_Motor_Torque_Control_Config(self):
        self.Torque = ttk.Label(self.torque_ctl_frame, text = "Target Iq ",state = "disabled")
        self.inputTorque = tk.Text(self.torque_ctl_frame, height=1, width=5, bg = "light cyan", state = "disabled" )
        self.torqueDuration = ttk.Label(self.torque_ctl_frame,text = "Durations",state = "disabled" )
        self.torqueRamping = tk.Text(self.torque_ctl_frame,height=1, width=5, bg = "light cyan", state = "disabled" )
        self.ExecTorqueRamp = ttk.Button(self.torque_ctl_frame, text = "Execute Ramp", state = "disabled")

    def UI_Motor_Torque_Control_PID_Config(self):
        self.Current_P = ttk.Label(self.torque_pid_frame, text="Kp",state = "disabled")
        self.Current_Kp = tk.Text(self.torque_pid_frame, height=1, width=5, bg = "light cyan",state = "disabled")
        self.Current_I  = ttk.Label(self.torque_pid_frame,text = "KI",state = "disabled")
        self.Current_KI = tk.Text(self.torque_pid_frame,height=1, width=5, bg = "light cyan",state = "disabled")

    def UI_PUT_MOTOR_MODE_FRAME(self):
        #Choosing Control Mode
        self.mode_frame.grid(column=0,row=100)
        self.mode_choose.grid(column = 0, row = 0)
        self.MOTOR_CHOICE.grid(column = 1, row = 0)
        self.CTL_OK.grid(column = 3, row = 0)
        #Speed Control 
        self.speed_ctl_frame.grid(column = 0 , row = 2, padx= 10, pady = 10)
        self.Speed.grid(column=1, row = 3, ipadx=5, ipady = 5)
        self.inputSpeed.grid(column = 2, row = 3, ipadx=8, ipady = 0)
        self.duration.grid(column = 1, row = 4,ipadx=11, ipady = 5 )
        self.ramping.grid(column = 2, row = 4, ipadx=8, ipady = 0  )
        self.Exec.grid(column = 2, row =6, ipadx=8, ipady=0)
        #Torque Control
        self.torque_ctl_frame.grid(column = 0, row = 10, padx= 10, pady = 10 )
        self.Torque.grid(column = 1, row = 3, ipadx=5, ipady = 5)
        self.inputTorque.grid(column = 2, row = 3, ipadx=8, ipady = 0 )
        self.torqueDuration.grid(column = 1, row = 4,ipadx=11, ipady = 5 )
        self.torqueRamping.grid(column = 2, row = 4, ipadx=8, ipady = 0)
        self.ExecTorqueRamp.grid(column = 2, row =6, ipadx=8, ipady=0)
        #PID Speed Control
        self.speed_pid_frame.grid(column = 1, row = 2, padx= 20, pady = 10 )
        self.Speed_P.grid(column = 1, row = 3, ipadx=11, ipady = 5)
        self.Speed_Kp.grid(column = 2, row = 3, ipadx=11, ipady = 0)
        self.Speed_I.grid(column = 1, row = 4,ipadx=13, ipady = 5)
        self.Speed_KI.grid(column = 2, row = 4, ipadx=11, ipady = 0 )
        #PID Torque Control
        self.torque_pid_frame.grid(column = 1, row = 10, padx= 20, pady = 10)
        self.Current_P.grid(column = 1, row = 3, ipadx=10, ipady = 5)
        self.Current_Kp.grid(column = 2, row = 3, ipadx=11, ipady = 0)
        self.Current_I.grid(column = 1, row= 4,ipadx=13, ipady = 5 )
        self.Current_KI.grid(column = 2, row = 4, ipadx=11, ipady = 0 )

    def mode_determine(self):
        if "Speed Mode" in self.motor.get():
            self.Exec["state"] = "active"
            self.inputSpeed["state"] = "normal"
            self.ramping["state"] = "normal"
            self.Speed["state"] = "normal"
            self.duration["state"] = "normal"
            self.Speed_P["state"] = "normal"
            self.Speed_Kp["state"] = "normal"
            self.Speed_I["state"] = "normal"
            self.Speed_KI["state"] = "normal"
            self.inputTorque["state"] = "disabled"
            self.torqueRamping["state"] = "disabled"
            self.ExecTorqueRamp["state"] = "disabled"
            self.Torque["state"] = "disabled"
            self.torqueDuration["state"] = "disabled"
            self.Current_P["state"] = "disabled"
            self.Current_Kp["state"] = "disabled"
            self.Current_I["state"] = "disabled"
            self.Current_KI["state"] = "disabled"
            print("1")
        elif "Torque Mode" in self.motor.get():
            self.Exec["state"] = "disable"
            self.inputSpeed["state"] = "disabled"
            self.ramping["state"] = "disabled"
            self.Speed["state"] = "disabled"
            self.duration["state"] = "disabled"
            self.Speed_P["state"] = "disabled"
            self.Speed_Kp["state"] = "disabled"
            self.Speed_I["state"] = "disabled"
            self.Speed_KI["state"] = "disabled"
            self.inputTorque["state"] = "normal"
            self.torqueRamping["state"] = "normal"
            self.ExecTorqueRamp["state"] = "active"
            self.Torque["state"] = "normal"
            self.torqueDuration["state"] = "normal"
            self.Current_P["state"] = "normal"
            self.Current_Kp["state"] = "normal"
            self.Current_I["state"] = "normal"
            self.Current_KI["state"] = "normal"
            print("2")

class UI_UART_CTL:
    def __init__(self,root):
        self.root = root
        self.UI_UART_FRAME()
        self.UI_UART_COM_CONFIG()
        self.UI_UART_BAUD_CONFIG()
        self.UI_UART_CONNECT()
        self.UI_UART_DISCONNECT()
        self.UI_UART_PORT_REFRESH()
        self.UI_SEND_MSG()
        self.MSG_LIST_CONFIG()
        self.UI_UART_SEND_MSG()
        self.UI_UART()

    def UI_UART_FRAME(self):
        self.uart_frame = ttk.LabelFrame(self.root, text='UART CONNECTION')

    def UI_SEND_MSG(self):
        self.uart_msg = ttk.LabelFrame(self.root, text = "Acknowledgement Status")               
    
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
        self.baud_choices = ttk.OptionMenu(self.uart_frame,self.baud,self.BAUD_LIST[0],*self.BAUD_LIST,command = self.uart_info)
    
    def MSG_LIST_CONFIG(self):
        self.msg_letter = ttk.Label(self.uart_msg, text = "Commands",width = 15)
        self.COMMAND = ['A','D','R','S']
        self.cmd = tk.StringVar(self.root)
        self.cmd.set(self.COMMAND)
        self.cmd_choices = ttk.OptionMenu(self.uart_msg,self.cmd,self.COMMAND[0], *self.COMMAND)

    def UI_UART_CONNECT(self):
        self.connect = ttk.Button(self.uart_frame,text = 'Connect',command=self.uart_connection_callback, state = "disabled")
    
    def UI_UART_DISCONNECT(self):
        self.disconnect = ttk.Button(self.uart_frame,text = 'Disconnect',command=self.uart_disconnect_callback, state = "disabled")
    
    def UI_UART_PORT_REFRESH(self):
        self.refresh = ttk.Button(self.uart_frame,text="Refresh COM", command=self.uart_port_search)
    
    def UI_UART_SEND_MSG(self):
        self.send = ttk.Button(self.uart_msg, text ="SEND", command=self.uart_msg_send, state='disabled')

    def UI_UART(self):
        self.uart_frame.grid(column = 0, row=0, padx=100, pady=30)
        self.uart_com_port.grid(column = 0, row = 1, ipadx=8, ipady= 0)
        self.uart_com_rate.grid(column = 0, row = 0, ipadx=8, ipady= 0)
        self.baud_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)
        self.COM_choices.grid(column=1,row=1,ipadx=10, ipady= 0)
        self.connect.grid(column=2,row=0,ipadx=10, ipady= 0)
        self.disconnect.grid(column=3,row=0,ipadx=10, ipady= 0)
        self.refresh.grid(column = 2,row=1,ipadx=10, ipady=0)
        self.uart_msg.grid(column = 100 ,row = 0, padx = 0, pady = 0)
        self.msg_letter.grid(column = 0 ,row = 0,ipadx=8, ipady= 0 )
        self.cmd_choices.grid(column = 1, row = 0, ipadx=10, ipady= 0)
        self.send.grid(column = 2, row = 0,ipadx=10, ipady= 0 )
    
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
            self.refresh["state"] = "disable"
            self.send['state'] = "active"
            ConnMsg = f"{self.COM.get()} is successfully connected !"
            messagebox.showinfo("UART",ConnMsg)

   
    def uart_disconnect_callback(self):
        self.STM32_UART.uartClose()
        print('Disconnected !')
        print(self.STM32_UART.uartStatus())
        if self.STM32_UART.uartStatus() is False:
            self.disconnect["state"] = "disable"
            self.refresh["state"] = "active"
            self.send['state'] = "disabled"
            DisMsg = f"{self.COM.get()} is disconnected !"
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
        self.COM_choices = ttk.OptionMenu(self.uart_frame,self.COM,self.COM_LIST[0],*self.COM_LIST,command=self.uart_info)
        self.COM_choices.grid(column=1,row=1,ipadx=10,ipady=0)
    
    def uart_msg_send(self):
        print(self.cmd.get())
        self.STM32_UART.uartWrite(self.cmd.get())

class MOTOR_OPERATION:
    def __init__(self,root):
        self.root = root
        self.UI_MOTOR_OPERATION_FRAME()
        self.UI_START_MOTOR()
        self.UI_STOP_MOTOR()
        self.UI_RESET_ERROR()