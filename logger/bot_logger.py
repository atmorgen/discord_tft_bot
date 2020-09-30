import asyncio
from jiffies.jiffies import JIFFY
from logger.barrel_roll import barrel_roll
class BotLogger:

    def __init__(self, message):
        self.message = message

    async def send_message(self, content):
        return await self.message.channel.send(content)

    async def edit_message(self, to_append):
        og_message = self.message.content
        new_message = og_message = og_message + f"\n {to_append}"
        await self.message.edit(content= new_message)

    async def i_broke_cause_rate_limit(self):
        og_message = self.message.content
        message = "Rate Limit Exceeded(count to 20)."
        jiffy = await JIFFY.get_random_giphy("chill")
        new_message = message + f"\n {jiffy}"
        await self.message.edit(content= new_message)

    async def do_a_barrel_roll(self):
        message = None
        for barrel in barrel_roll:
            await asyncio.sleep(1)
            if message == None:
                message = await self.message.channel.send(barrel)
            else:
                await message.edit(content= barrel)

    def set_message(self, message):
        self.message = message