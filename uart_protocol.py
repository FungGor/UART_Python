# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html
# https://sites.google.com/site/greenmechatroniks/code-garage/rs-232-pyserial-in-python

import serial
import serial.tools.list_ports

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

class UART_SETTING:
     def __init__(self, portID, baudrate, parity, stopbits, bytesize, timeout, protocol):
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

     
     def uartOpen(self):
          self.protocol = serial.Serial()
          self.protocol.parity = self.parity
          self.protocol.baudrate = self.baudrate
          self.protocol.port = self.portID
          self.protocol.stopbits = self.stopbits
          self.protocol.open()
     
     def uartRead(self):
        self.protocol.readline()

     def uartWrite(self,byte):
         self.protocol.write(byte)
     
     def uartClose(self):
         self.protocol.close()
    
     def uartStatus(self):
         return self.protocol.isOpen()
      
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
         print(self.parity)
         return self.parity
      
     def uart_STOPBIT_Config(self):
         match self.stopbits:
           case 1:
              self.stopbits = serial.STOPBITS_ONE
           case 1.5:
              self.stopbits = serial.STOPBITS_ONE_POINT_FIVE
           case 2:
              self.stopbits = serial.STOPBITS_TWO
         print(self.stopbits)
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
         print(self.bytesize)
         return self.bytesize


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