# This is an automated data logging system of STM32 Motor Controller
# Users can make use of STM32 Motor Control Protocol to retrieve the motors' parameters & status to work on the evalution
# For more details, users are required to read the STM32MCP SDK Datasheet
# This software is compible to Windows, MacOS and Linux Platform
# For the hardware implementation's purpose, users are suggested to use MacOS or Linux Platform
# During dyno's testing, it is encouraged to implement this Real Time software into the Raspberry Pi! 

import matplotlib
import tkinter as tk
import threading
import STM32MCP_Lib
