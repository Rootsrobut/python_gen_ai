import threading

chai_stock = 0
#stock_lock = threading.Lock() 

def restock():
    global chai_stock
    #stock_lock.acquire()
    try:
        for _ in range(100000):
            chai_stock += 1
    finally:
        #stock_lock.release()
        pass


threads = [threading.Thread(target=restock) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final chai stock: {chai_stock}")