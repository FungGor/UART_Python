import threading
import time
import signals
import STM32MCP_CTL

RETRANSMISSION_INTERVAL = 0.5  # Interval in seconds for retransmission, 500 ms

def retransmission_handler():
    while running:
        # Here you would implement the actual retransmission logic
        # For example, checking if there are messages in the queue that need to be retransmitted.
        # This is a placeholder for the actual retransmission logic.
        # Simulate retransmission delay
        STM32MCP_CTL.ECU_Protocol_Retransmission()
        time.sleep(RETRANSMISSION_INTERVAL)

def start_retransmission_thread():
    global running, retransmission_thread
    running = True
    retransmission_thread = threading.Thread(target=retransmission_handler, daemon=True)
    retransmission_thread.start()

def stop_retransmission_thread():
    global running, retransmission_thread
    running = False
    retransmission_thread.join()
