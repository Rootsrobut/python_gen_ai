import threading
import time

def prepare_chai(type_,wait_time):
    print(f'{type_} chai: brewing...')
    time.sleep(wait_time)
    print(f'{type_} chai:Ready...')
    

start=time.time()
t1=threading.Thread(target=prepare_chai,args=('Masala',3))
t2=threading.Thread(target=prepare_chai,args=('tulsi',2))

t1.start()
t2.start()
t1.join()
t2.join()
end=time.time()

print(f'chai is  ready in {end-start:.2f} seconds')
