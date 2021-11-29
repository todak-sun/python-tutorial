import asyncio
import time

async def main():
    print('start')
    await asyncio.sleep(1)
    print('end')

start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)