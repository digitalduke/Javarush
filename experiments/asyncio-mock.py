import asyncio


async def routine():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


async def infinity_routine():
    while True:
        print('tik ...')
        await asyncio.sleep(1)
        print('... tok!')


# one-time
print('one-time')
loop = asyncio.get_event_loop()
loop.run_until_complete(routine())


# forever
print('forever')
asyncio.ensure_future(infinity_routine())
loop.run_forever()
