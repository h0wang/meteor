import asyncio
import websockets


class Subscriber:

    def __init__(self, subscription, queue):
        self.queue = queue
        self.subscription = subscription

    async def subscribe(self):
        request = self.subscription.request
        parser = self.subscription.parser
        uri = self.subscription.uri
        async with websockets.connect(uri) as socket:
            await socket.send(request)
            async for msg in socket:
                parsed = parser(msg)
                # print(msg)
                if parsed is not None:
                    # print(parsed)
                    await self.queue.put(parsed)
