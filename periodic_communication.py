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
protocol = True

class ProtocolEventHandler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Set the thread as a daemon thread
        self.protocol_thread = threading.Event()  # Event to control the thread
        self.protocol_thread.set()
      
    def run(self):
        global TICK
        while protocol:
            if TICK % 1 == 0: # Every 1 tick, which equals 0.02 seconds
               STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_VOLTAGE)
               STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_CURRENT)
               STM32MCP_CTL.STM32MCP_controlEscooterBehavior(STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_TEMPERATURE)
            elif TICK % 25 == 0: # Every 25 ticks, which equals 0.5 seconds
               STM32MCP_CTL.ECU_RetransmitHandling()
            TICK += 1
            self.protocol_thread.wait(timeout=TIMER_INTERVAL) #Block until the event is set or the timeout occurs
    
    def pause(self):
        self.protocol_thread.clear()  # Stop the thread by clearing the event
   
    def resume(self):
        self.protocol_thread.set()    # Resumer the thread by setting the event

def run_protocol_event_handler():
    global protocol_event_handler
    protocol_event_handler = ProtocolEventHandler()
    protocol_event_handler.start()

def stop_protocol_event_handler():
    protocol_event_handler.pause()  # Pause the thread

def resume_protocol_event_handler():
    protocol_event_handler.resume()  # Resume the thread
        


 
    
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

