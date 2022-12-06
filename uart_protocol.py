# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html
# https://sites.google.com/site/greenmechatroniks/code-garage/rs-232-pyserial-in-python

import serial

# @Class UART
# @brief     It defines a set of member unctions that the server
#            wants to point to the application functions
# @data      uartOpen:   Called when the application wants to initialize the uart peripheral
#            uartWrite:  Called when the application wants to write to the uart peripheral
#            uartRead:   Called when the application wants to read from the uart peripheral
#            uartClose:  Called when the application wants to terminate the uart peripheral
#            uartStatus: Called when the application wants to check whether the uart peripheral is connected 

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