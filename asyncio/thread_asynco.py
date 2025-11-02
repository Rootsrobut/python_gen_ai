import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    # 1. FIX: Correctly get the event loop
    loop = asyncio.get_running_loop()
    # 2. FIX: Correct ThreadPoolExecutor usage and assignment
    with ThreadPoolExecutor() as pool: 
        # loop.run_in_executor offloads the blocking check_stock call to a thread in the pool
        result = await loop.run_in_executor(pool,check_stock, "Masala chai")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())