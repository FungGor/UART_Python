# https://www.section.io/engineering-education/how-to-perform-threading-timer-in-python/
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
# https://maldus512.medium.com/how-to-setup-correctly-an-application-with-python-and-tkinter-107c6bc5a45

import threading
import time
import STM32MCP_CTL
import STM32MCP_Lib

TIMER_INTERVAL = 0.02 # Interval in seconds for periodic communication
TICK = 0
TRANSMIT = True  # Flag to control transmission
def periodic_communication(serial):
    global TICK, TRANSMIT
    while True:
         # Here you would implement the actual communication logic
         # For example, sending a request to the STM32 motor controller
         # and processing the response.
         # This is a placeholder for the actual communication logic.
         # Simulate communication delay
         if TICK%1 == 0 and TRANSMIT is True: # Every 1 tick, which equals 0.02 seconds
            STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_VOLTAGE)
            STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_CURRENT)
            STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_TEMPERATURE)
         if TICK % 25 == 0 and TRANSMIT is False: # Every 50 ticks, which equal 0.5 seconds
            STM32MCP_CTL.ECU_RetransmitHandling()
            TRANSMIT = True

         TICK+=1
         time.sleep(TIMER_INTERVAL)

def run_periodic_communication(serial):
   timer_thread = threading.Thread(target=periodic_communication,args=(serial,), daemon=True)
   timer_thread.start()

