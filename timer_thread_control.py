# https://www.section.io/engineering-education/how-to-perform-threading-timer-in-python/
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679


import threading, time, signal
from datetime import timedelta

STM32MCP_TRANSMISSION_INTERVAL = 0.02 #sends commands in every 20ms

class ProgramKilled(Exception):
    pass

def send_command():
    #Retrieves speed, voltage, current, error status from the motor controller
    return 0

def signal_handler(signum, frame):
    raise ProgramKilled

class Start_Protocol(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)
    
    def start_cmd(self):
          #Those commands must be triggered by ( GUI event )
          signal.signal(signal.SIGTERM, signal_handler)
          signal.signal(signal.SIGINT, signal_handler)
          command_open = Start_Protocol(interval=timedelta(seconds=STM32MCP_TRANSMISSION_INTERVAL), execute=send_command)
          while True: 
                try:
                      time.sleep(0.02)
                except ProgramKilled:
                      command_open.stop()
                      break