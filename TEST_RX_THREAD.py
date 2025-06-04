#The script tests for UART's functionalities
import periodic_communication
import threading
import STM32MCP_CTL
import STM32MCP_Lib
import uart_protocol


# Initialize the UART communication1
uartObj = STM32MCP_CTL.STM32MCP_Init()
STM32MCP_CTL.MsgQueueInit()
print("isInitialized ? :", uartObj.uartInit())
print("isOpened ? ", uartObj.uartOpen())
print("Status ? ",uartObj.connectionStatus())


ser = uartObj.take_serial_obj()
uart_protocol.startRxThread(ser,uartObj)
