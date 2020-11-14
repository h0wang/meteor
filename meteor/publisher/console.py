import asyncio

from .base import Publisher


class ConsolePublisher(Publisher):

    def __init__(self, queue):
        self.queue = queue

    async def publish(self):
        while True:
            item = await self.queue.get()
            if item is None:
                break
            print(item)
