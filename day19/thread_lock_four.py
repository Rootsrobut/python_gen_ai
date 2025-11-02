import  threading
import time
counter=0
lock=threading.Lock()
def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter +=1
            
threads=[threading.Thread(target=increament) for _ in range(10)]

start=time.time()
[t.start() for t in threads]    
[t.join() for t in threads] 
end=time.time()        



print(f'Final counter: {counter} and Total time is taken to run the program {end-start}') 