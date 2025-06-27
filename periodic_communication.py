# https://www.section.io/engineering-education/how-to-perform-threading-timer-in-python/
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
# https://maldus512.medium.com/how-to-setup-correctly-an-application-with-python-and-tkinter-107c6bc5a45

import threading
import time
import STM32MCP_CTL
import STM32MCP_Lib   

TIMER_INTERVAL = 0.02 # Interval in seconds for periodic communication
TICK = 0
LossCount = 0
retransmit = True

def periodic_communication():
    global TICK, LossCount
    while True:
        STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_VOLTAGE)
        STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_CURRENT)
        STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_TEMPERATURE)
        STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_DRIVER_TEMP)
        STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_TIMEOUT_CHECKING)
        if TICK%25 == 0 and retransmit:
            LossCount += 1
            print(f"Loss Count: {LossCount}")
            STM32MCP_CTL.retransmissionHandler()
        TICK+=1
        time.sleep(TIMER_INTERVAL)  # Simulate some processing time

def run_periodic_communication():
   timer_thread = threading.Thread(target=periodic_communication, daemon=True)
   timer_thread.start()

def lossReset():
    global LossCount
    LossCount = 0

def stopRetransmit():
    global retransmit
    retransmit = False

def startRetransmit():
    global retransmit
    retransmit = True