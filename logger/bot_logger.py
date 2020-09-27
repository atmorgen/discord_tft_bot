class BotLogger:

    def __init__(self, message):
        self.message = message

    async def send_message(self, content):
        return await self.message.channel.send(content)

    async def edit_message(self, to_append):
        og_message = self.message.content
        new_message = og_message = og_message + f"\n {to_append}"
        await self.message.edit(content= new_message)

    def set_message(self, message):
        self.message = message