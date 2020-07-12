import asyncio
import json

from dbus_next.message import Message, MessageType
from dbus_next.aio import MessageBus


async def infinity_routine():
    bus = await MessageBus().connect()

    reply = await bus.call(
        Message(
            path='/org.freedesktop.Notifications',
            interface='org.freedesktop.Notifications',
            member='Notify'
        )
    )

    if reply.message_type == MessageType.ERROR:
        raise Exception(reply.body[0])

    print(json.dumps(reply.body[0], indent=2))


loop = asyncio.get_event_loop()
asyncio.ensure_future(infinity_routine())

loop.run_forever()
