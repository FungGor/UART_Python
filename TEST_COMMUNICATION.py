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

Command = int(input("Enter command (1: Start, 2: Send, 3: Check, 4: Stop): "))

match Command:
    case 1:
        print("Starting UART Communication...")
    
    case 2:
        print("Sending command to STM32 device...")

    case 3:
        print("Checking status of UART Communication...")
    
    case 4:
        print("Stopping UART Communication...")


