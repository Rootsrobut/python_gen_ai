from multiprocessing import Process, Value

def increment(counter):
    """Increments the shared counter 100,000 times,using the lock to ensure mutual exclusion."""
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__ == '__main__':
    # Create a shared integer ('i') Value initialized to 0.
    # The lock for synchronization is created automatically with the Value.
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print("Final counter value:", counter.value)