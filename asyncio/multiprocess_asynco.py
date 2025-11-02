import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data: str) -> str:
    return f"® {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        print("Starting encryption in a separate process...")
        data_to_encrypt = "credit_card_1234"
        result = await loop.run_in_executor(
            pool,           
            encrypt,      
            data_to_encrypt 
        )
        
        print(f"Encryption Complete. Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())