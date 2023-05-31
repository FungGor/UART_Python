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

import matplotlib
import tkinter
import threading
import STM32MCP_Lib
import serial
