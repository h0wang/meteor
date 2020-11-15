import asyncio
import abc


class Publisher:

    @abc.abstractmethod
    async def publish(self):
        raise NotImplementedError
