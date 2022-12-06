# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
import serial

class uart_init():
     def __init__(self, baudrate, parity, stopbits, bytesize, timeout):
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
     
     def uart_Open(self):
        ser = serial.Serial("COM8",baudrate = self.baudrate, parity = self.parity, 
        stopbits = self.stopbits, 
        bytesize = self.bytesize,
        timeout = self.timeout)