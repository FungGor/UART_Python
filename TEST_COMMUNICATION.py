import periodic_communication
import threading
import STM32MCP_CTL
import STM32MCP_Lib
import uart_protocol

# Initialize the UART communication
uartObj = STM32MCP_CTL.STM32MCP_Init()
# Try to communicate with the STM32 device
# 1 -- Start UART Communication
# 2 -- Send a command to the STM32 device
# 3 -- Check Status of UART Communication
# 4 -- Stop UART Communication
InputFinished = 0
try:
    global Command
    while True:
        if InputFinished == 0:
            Command = int(input("Enter command (1: Init, 2: Open, 3: Check, 4: Stop): "))
            InputFinished = 1
        elif InputFinished == 1:
            if Command == 1:
                print("isInitialized ? :", uartObj.uartOpen())
                InputFinished = 0
            elif Command == 2:
                print("isOpened ? ", uartObj.connectionStatus())
                InputFinished = 0

except KeyboardInterrupt:
    print("Loop Finished")
    
    
        




