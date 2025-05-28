import threading
import time

RETRANSMISSION_INTERVAL = 0.5  # Interval in seconds for retransmission

def retransmission_handler():
    while True:
        print("Retransmission task started.")
        # Here you would implement the actual retransmission logic
        # For example, checking if there are messages in the queue that need to be retransmitted.
        # This is a placeholder for the actual retransmission logic.
        # Simulate retransmission delay
        time.sleep(RETRANSMISSION_INTERVAL)
        print("Retransmission task completed.")

def start_retransmission():
    retransmission_thread = threading.Thread(target=retransmission_handler, daemon=True)
    retransmission_thread.start()