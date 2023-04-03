from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from button import RelaySwitch


class MyComponent(ApplicationSession):

    async def onJoin(self, details):
        print("Procedure registered")
        registration = RelaySwitch()
        regs = await self.register(registration)
        for reg in regs:
            print("registered", reg.procedure)

if __name__ == '__main__':
    url = environ.get("wick", "ws://localhost:8080/ws")
    realm = "realm1"
    runner = ApplicationRunner(url, realm)
    runner.run(MyComponent)