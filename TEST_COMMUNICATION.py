#Scripts for UART Communication Testing
import periodic_communication
import threading
import STM32MCP_CTL
import STM32MCP_Lib
import uart_protocol

# Initialize the UART communication
uartObj = STM32MCP_CTL.STM32MCP_Init()
STM32MCP_CTL.MsgQueueInit()
# Try to communicate with the STM32 device
# 1 -- Start UART Communication
# 2 -- Send a command to the STM32 device
# 3 -- Check Status of UART Communication
# 4 -- Stop UART Communication
InputFinished = 0
DataNumber = 0
try:
    global Command
    bytes_sent = 0
    while True:
        if InputFinished == 0:
            Command = int(input("Enter command (1: Init, 2: Open, 3: Check, 4: List, 5: Send Datagram, 6: Close Serial Port): "))
            InputFinished = 1
        elif InputFinished == 1:
            if Command == 1:
                print("isInitialized ? :", uartObj.uartInit())
                InputFinished = 0
            elif Command == 2:
                print("isOpened ? ", uartObj.uartOpen())
                InputFinished = 0
            elif Command == 3:
                print("Status ? ",uartObj.connectionStatus())
                InputFinished = 0
            elif Command == 4:
                uartObj.listPorts()
                InputFinished = 0
            elif Command == 5:
                if DataNumber == 0:
                    datagram = STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_1)
                    print("Test Datagram: ", [hex(b) for b in datagram])
                    bytes_sent = uartObj.uartWrite(datagram)
                    print("Number of bytes sent ; {}".format(bytes_sent))
                    DataNumber = 1
                    InputFinished = 0
                elif DataNumber == 1:
                    datagram = STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_2)
                    print("Test Datagram: ", [hex(b) for b in datagram])
                    bytes_sent = uartObj.uartWrite(datagram)
                    print("Number of bytes sent ; {}".format(bytes_sent))
                    DataNumber = 2
                    InputFinished = 0
                elif DataNumber == 2:
                    datagram = STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_3)
                    print("Test Datagram: ", [hex(b) for b in datagram])
                    bytes_sent = uartObj.uartWrite(datagram)
                    print("Number of bytes sent ; {}".format(bytes_sent))
                    DataNumber = 0
                    InputFinished = 0
            elif Command == 6:
                    uartObj.uartClose()
                    InputFinished = 0

except KeyboardInterrupt:
    print("Loop Finished")
    
    
        




