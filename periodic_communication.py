# https://www.section.io/engineering-education/how-to-perform-threading-timer-in-python/
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
# https://maldus512.medium.com/how-to-setup-correctly-an-application-with-python-and-tkinter-107c6bc5a45

import threading
import time
import STM32MCP_CTL
import STM32MCP_Lib

TIMER_INTERVAL = 3  # Interval in seconds for periodic communication

def periodic_communication():
    while True:
       STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_1)
       STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_2)
       STM32MCP_CTL.Test_Datagram(STM32MCP_Lib.TEST_CASE_3)
       time.sleep(TIMER_INTERVAL)  # Simulate some processing time
    # Here you would implement the actual communication logic
    # For example, sending a request to the STM32 motor controller
    # and processing the response.
    # This is a placeholder for the actual communication logic.
    # Simulate communication delay

def run_periodic_communication():
   timer_thread = threading.Thread(target=periodic_communication, daemon=True)
   timer_thread.start()
