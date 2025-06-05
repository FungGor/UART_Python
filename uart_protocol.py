# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html
# https://sites.google.com/site/greenmechatroniks/code-garage/rs-232-pyserial-in-python

# https://pyserial.readthedocs.io/en/latest/pyserial_api.html --> Threading Required
# Ensure the Libraies' functionalities, then implement Logging Library

#Low Level Peripheral which access Hardware Level Layer
from base64 import encode
import serial
import serial.serialutil
import serial.tools.list_ports
from serial.serialutil import SerialException
import serial.threaded
import time
import logging
import string

# @Class UART
# @brief     It defines a set of member unctions that the server
#            wants to point to the application functions
# @data      uartOpen:      Called when the application wants to initialize the uart peripheral
#            uartWrite:     Called when the application wants to write to the uart peripheral
#            uartRead:      Called when the application wants to read from the uart peripheral
#            uartClose:     Called when the application wants to terminate the uart peripheral
#            uartStatus:    Called when the application wants to check whether the uart peripheral is connected 
#            uartParaConfig: It must be called before using the another functions defined in UART_Protocol class
#
# For STM32 FOC Motor Control SDK, we have the following UART Configurations:
# BAUD RATE   = 115200
# WORD Length = 8-BIT
# STOP BITS   = STOPBITS_1
# PARITY      = UART_PARITY_NONE

class UART_Protocol():
     def __init__(self, portID, baudrate, parity, stopbits, bytesize, timeout, protocol, status_connect):
        self.portID = portID
        self.baudrate = baudrate
        self.parity = parity
        self.parity = self.uart_Parity_Config()
        self.stopbits = stopbits
        self.stopbits = self.uart_STOPBIT_Config()
        self.bytesize = bytesize
        self.bytesize = self.uart_BYTESIZE_Config()
        self.timeout = timeout
        self.protocol = protocol
        self.status_connect = status_connect
      
     def listPorts(self):
         port_list = serial.tools.list_ports.comports()
         print("Listing ports......")
         for com_port, port_des, hwid in sorted(port_list):
             print("{}: {} [{}]".format(com_port,port_des,hwid))
             print("\n")
     
     def uartInit(self) -> bool:
         print("Attempting to initialize Serial Protocol.....")
         try:
               self.protocol = serial.Serial()                            
               self.status_connect = 1
               time.sleep(0.3)
               return True
         except serial.serialutil.SerialException as e:
            print(f"Error : {e}")
            self.status_connect = -1
            return False
      
     def uartOpen(self) -> bool:
         if self.status_connect == 1:
            self.protocol.port=self.portID
            self.protocol.baudrate=self.baudrate
            self.protocol.parity=self.parity
            self.protocol.stopbits=self.stopbits
            self.protocol.bytesize=self.bytesize
            self.protocol.timeout=self.timeout
            time.sleep(0.3)
            self.protocol.open()
            return True
         else:
            print("Serial Port is Not Initialized")
         return False

     def connectionStatus(self) -> string:
            message = ''
            #What's the status of Serial Connection??
            if self.status_connect == -1:
               message += 'Warning : Serial Connection Error'
            
            if self.status_connect == 0:
               message += 'Serial Port Closed'
               
            if self.status_connect == 1:
               try:
                  message += '\nSerial Status: ' + str(self.protocol.is_open)
               except Exception as e:
                   message+='Fatal Fault'                     
            return message

     def uartFaultHandler(self) -> bool:
         print("How to Handle the Fault?")
         return False
                      
     def uartRead(self):
        self.protocol.readline()

     #Send it byte by byte
     def uartWrite(self, data: bytearray) -> int:
         data_bytes = 0
         if self.protocol.is_open:
            data_bytes = self.protocol.write(data)
         else:
             print("Warning : Serial Port is not available")
         return data_bytes
     
     def uartClose(self) -> bool:
         print("Closing Serial Port..........")
         if self.status_connect == 1:
             try:
                 self.protocol.close()
                 print("Serial Port is successfully closed")
                 self.status_connect = 0
                 return True
             except Exception as e:
                 print("Serial Closure Fatal Error!")
                 print(f"Fault: ",e)
                 self.status_connect = -1
                 return False
         
         if self.status_connect == 0:
             print("Serial Port is already closed")
         
         if self.status_connect == -1:
             print("Warning : Serial Faults")
         return False
                               
     def uartStatus(self) -> bool:
         #Gets the state of serial port, whether is open
         return self.protocol.is_open
      
     def uart_Parity_Config(self):
         match self.parity:
            case 'NONE':
               self.parity = serial.PARITY_NONE
            case 'EVEN':
               self.parity = serial.PARITY_EVEN
            case 'ODD':
                self.parity = serial.PARITY_ODD
            case 'MASK':
                self.parity = serial.PARITY_MARK
            case 'SPACE':
                self.parity = serial.PARITY_SPACE
         print("Parity Bits : ",self.parity)
         return self.parity
      
     def uart_STOPBIT_Config(self):
         match self.stopbits:
           case 1:
              self.stopbits = serial.STOPBITS_ONE
           case 1.5:
              self.stopbits = serial.STOPBITS_ONE_POINT_FIVE
           case 2:
              self.stopbits = serial.STOPBITS_TWO
         print("Stop Bits : ",self.stopbits)
         return self.stopbits
      
     def uart_BYTESIZE_Config(self):
         match self.bytesize:
            case 5:
               self.bytesize = serial.FIVEBITS
            case 6:
               self.bytesize = serial.SIXBITS
            case 7:
               self.bytesize = serial.SEVENBITS
            case 8:
               self.bytesize = serial.EIGHTBITS
         print("WORD LENGTH : ",self.bytesize)
         return self.bytesize
     
     def take_serial_obj(self):
         return self.protocol
         


InputFinished = 0
DataNumber = 0
Command = 0

receivedBuffer = bytearray()

def showAllReceivedBytes():
    print("{} bytes received.".format(len(receivedBuffer)))
    print(" ".join(f"{b:02X}" for b in receivedBuffer))

#UART Rx Interrupt i.e. Threading
#Better to create array to store incoming data
class ByteReceiver(serial.threaded.Protocol):
    def __init__(self):
        super().__init__()
    
    def data_received(self, data):         
         for b in data:
             #print(f"Received byte: {b:02X}")
             receivedBuffer.append(b)
         showAllReceivedBytes()
         
         

def startRxThread(ser,obj):
    global Command
    global InputFinished
    with serial.threaded.ReaderThread(ser,ByteReceiver) as protocol:
        print("Listening for bytes, Press Ctrl+C to exit")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Exiting RX ISR")
         
#Scanning the available ports
class UART_SCAN():
   def __init__(self):
      pass
   
   def com_scan(self,com_port):
      self.port = com_port
      self.scanning = serial.tools.list_ports.comports()
      for scanning, description, PORT_ID in sorted(self.scanning):
         print("{}: {} [{}]".format(scanning,description,PORT_ID))
         print(scanning)
         self.port.append(scanning)
      return self.port