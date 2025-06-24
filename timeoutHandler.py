import threading
import time
import STM32MCP_CTL

execute = True
i = 0
class TimeOutThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Set the thread as a daemon thread
        self._timeout_event = threading.Event()
        self._timeout_event.set()  # Start in a non-paused state

    def run(self):
        global i
        while execute:
            i += 1
            self._timeout_event.wait()  # Block the thread if paused
            #print(f"Running... {i}")
            STM32MCP_CTL.ECU_RetransmitHandling()
            time.sleep(0.5)  # Simulating work

    def pause(self):
        self._timeout_event.clear()  # Pause the thread

    def resume(self):
        self._timeout_event.set()  # Resume the thread

# Usage
def timeOutStart():
    global timeout_thread
    timeout_thread = TimeOutThread()
    timeout_thread.start()
    #timeout_thread.join()

def timeOutPause():
    timeout_thread.pause()

def timeOutResume():
    #print("Resuming thread...")
    timeout_thread.resume()