# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html
# https://sites.google.com/site/greenmechatroniks/code-garage/rs-232-pyserial-in-python

import serial

# @Class UART
# @brief     It defines a set of member unctions that the server
#            wants to point to the application functions
# @data      uartOpen:      Called when the application wants to initialize the uart peripheral
#            uartWrite:     Called when the application wants to write to the uart peripheral
#            uartRead:      Called when the application wants to read from the uart peripheral
#            uartClose:     Called when the application wants to terminate the uart peripheral
#            uartStatus:    Called when the application wants to check whether the uart peripheral is connected 
#            uartParaConfig: It must be called before using the another functions defined in UART_Protocol class

class UART_Protocol:
     def __init__(self, portID, baudrate, parity, stopbits, bytesize, timeout, protocol):
        self.portID = portID
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
        self.protocol = protocol
     
     def uartOpen(self):
         if self.protocol == None:
           self.protocol = serial.Serial(self.portID,baudrate = self.baudrate, parity = self.parity, 
           stopbits = self.stopbits, 
           bytesize = self.bytesize,
           timeout = self.timeout)
           self.protocol.open()
     
     def uartRead(self):
        self.protocol.readline()

     def uartWrite(self,byte):
         self.protocol.write(byte)
     
     def uartClose(self):
         self.protocol.close()
    
     def uartStatus(self):
         return self.protocol.isOpen()
      
     def uartParaConfig(self):
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
         
         match self.stopbits:
            case 1:
               self.stopbits = serial.STOPBITS_ONE
            case 1.5:
               self.stopbits = serial.STOPBITS_ONE_POINT_FIVE
            case 2:
               self.stopbits = serial.STOPBITS_TWO
         
         match self.bytesize:
            case 5:
               self.bytesize = serial.FIVEBITS
            case 6:
               self.bytesize = serial.SIXBITS
            case 7:
               self.bytesize = serial.SEVENBITS
            case 8:
               self.bytesize = serial.EIGHTBITS
            
