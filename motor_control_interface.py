# This is an automated data logging system of STM32 Motor Controller
# Users can make use of STM32 Motor Control Protocol to retrieve the motors' parameters & status to work on the evalution
# For more details, users are required to read the STM32MCP SDK Datasheet
# This software is compible to Windows, MacOS and Linux Platform
# For the hardware implementation's purpose, users are suggested to use MacOS or Linux Platform
# During dyno's testing, it is encouraged to implement this Real Time software into the Raspberry Pi! 
# It is used for testing for the motor's power efficienct Pout/Pin
# It could be used to simulate the dashboard's environment for debugging purpose
# For the advanced data analysis, it might be required to upload the logged data to Google Drive
# For more information, please go to https://developers.google.com/drive/api/quickstart/python
# Reference : https://www.youtube.com/watch?v=u3NnzRIwjH8&list=PLtVUYRe-Z-meHdTlzqCHGPjZvnL2VZVn8&index=2
#             https://www.pythontutorial.net/tkinter/

#from GUICTL import UI_INIT,UI_UART_CTL,UI_Motor_CTL_Mode

#stm32MCP = UI_INIT()
#stm32Config = UI_UART_CTL(stm32MCP.root)
#stm32MCPCTL = UI_Motor_CTL_Mode(stm32MCP.root)
#stm32MCP.root.mainloop()
import periodic_communication
import STM32MCP_CTL
periodic_communication.run_periodic_communication()

while True:
   pass# Keep the main thread alive to allow periodic communication to run