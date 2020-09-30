import logging
import discord
from tft_discord_bot import TFTDiscordBot
from config import DISCORD_TOKEN

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("discord").setLevel(logging.WARNING)


class TFTDiscordStartup(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.author == "Hiphopaplottamus#7024":
            await message.channel.send("Shut up, Max")
        
        await TFTDiscordBot.process_message(message)

    async def on_ready(self):
        logging.info(f"{self.user} has connected to Discord!")


client = TFTDiscordStartup()

client.run(DISCORD_TOKEN)
