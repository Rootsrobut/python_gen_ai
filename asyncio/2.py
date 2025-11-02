import asyncio
import time

async def brew(name):
    print(f"☕️ Brewing {name}...")
    # await asyncio.sleep(3)
    time.sleep(3)
    print(f"🎉 {name} is ready! (Finished at {time.strftime('%X')})")

async def main():
    # Uses asyncio.gather to run multiple brew tasks concurrently
    print(f"Starting brew tasks concurrently at {time.strftime('%X')}...")
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )
    print("All chai tasks are complete.")

# This is the single, correct way to run the top-level async function
if __name__ == "__main__":
    asyncio.run(main())