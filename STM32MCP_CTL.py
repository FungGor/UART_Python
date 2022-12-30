#This library implements the functions for controllling the STM32 Motor Driver (Applicable for F1xxx and F4xxx Series) 
import STM32MCP_Lib

#define UART Configuration Parameters 
#Create UART Objects
UART_PORT  = "COM3"
BAUD_RATE  = 9600
PARITY     = 'NONE'
STOPBITS   = 1
BYTE_SIZE  = 8
TIMEOUT    = None
uart_Event = None
uart = STM32MCP_Lib.STM32MCP_uartManager_t(UART_PORT,BAUD_RATE,PARITY,STOPBITS,BYTE_SIZE,TIMEOUT,uart_Event)


