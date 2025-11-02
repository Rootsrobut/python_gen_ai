import time
import threading

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2) 

# Create the thread, specifying the target function and setting it as daemon
t = threading.Thread(target=monitor_tea_temp, daemon=True)

# daemon=True
# non-daemon remove this only 
t.start()

print("Main program done")
