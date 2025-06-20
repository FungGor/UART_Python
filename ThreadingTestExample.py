#The script tests for UART's functionalities
import periodic_communication
import threading
import STM32MCP_CTL
import STM32MCP_Lib
import uart_protocol
import time

#Queue and Periodic Communication
STM32MCP_CTL.MsgQueueInit()  # Initialize the message queue

# 3) Test the periodic communication functionality --> Simulates hardware timer interrupt(Done)

uart_protocol.protocolControlInit()

# Initialize the UART communication1
uartObj = uart_protocol.UART_Init()
STM32MCP_CTL.STM32_SERIAL_PORT_INIT()

#Starts UART Interrupt
ser = uartObj.take_serial_obj()
uart_protocol.runRxInterrupt(ser, uartObj)

#Sends datagram periodically
periodic_communication.run_periodic_communication(uartObj)

STM32MCP_CTL.STM32MCP_CommunicationProtocol.STM32MCP_startCommunication()

#Equivalent to RTOS Start
try:
   # Keep the main thread alive, but allow for graceful exit with Ctrl+C
   while True:
       pass
except KeyboardInterrupt:
     print("Main program exiting.")
