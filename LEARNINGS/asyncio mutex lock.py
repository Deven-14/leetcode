import asyncio

lock = asyncio.Lock()

async def abc(log):
    async with lock:
        print(1, log, "start")
        await asyncio.sleep(3)
        print(1, log, "end")

async def abc2(log):
    print(2, log, "start")
    await abc(log)
    print(2, log, "end")
    
async def main():
    await asyncio.gather(abc2("a"), abc2("b"), abc2("c"))

asyncio.run(main())
# https://docs.python.org/3/library/asyncio-sync.html
