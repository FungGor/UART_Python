#The script tests for UART's functionalities
import periodic_communication
import threading
import STM32MCP_CTL
import STM32MCP_Lib
import uart_protocol
import time

#Queue and Periodic Communication
STM32MCP_CTL.MsgQueueInit()  # Initialize the message queue
#create a stop event
stop_event = threading.Event()
# 3) Test the periodic communication functionality --> Simulates hardware timer interrupt(Done)


# Initialize the UART communication1
uartObj = STM32MCP_CTL.STM32MCP_Init()
print("isInitialized ? :", uartObj.uartInit())
print("isOpened ? ", uartObj.uartOpen())
print("Status ? ",uartObj.connectionStatus())

#Starts UART Interrupt
ser = uartObj.take_serial_obj()
rx_thread = threading.Thread(target=uart_protocol.startRxThread, args=(ser, uartObj), daemon=True)
rx_thread.start()
periodic_communication.run_periodic_communication(uartObj)

counter = 0
try:
   # Keep the main thread alive, but allow for graceful exit with Ctrl+C
   while True:
       pass
except KeyboardInterrupt:
     print("Main program exiting.")
