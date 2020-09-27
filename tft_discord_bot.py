import logging
from items.item_processor import ItemProcessor
from averages.average_processor import AverageProcessor
from utilities.utility_tools import UtilityTools
from logger.bot_logger import BotLogger

class TFTDiscordBot:

	def __init__(self, client):
		logging.info("starting up tft bot")
		# self.puuid = UtilityTools.get_puuid()
		# self.match_array = UtilityTools.get_puuid_matches(self.puuid)

	@staticmethod
	async def process_message(message):
		
		bot_logger = BotLogger(message)
	
		if str(message.channel) == "tft_bot_channel":
			if message.content == "Slave Bot, Say Hello":
				await bot_logger.send_message("Hello!")

			split_message = message.content.split(" ")
			if split_message[0] == "TFT:":
				bot_logger.set_message(await bot_logger.send_message(f'processing average for {split_message[1]}.  this will take a bit'))

				puuid = UtilityTools.get_puuid(split_message[1])
				match_array = UtilityTools.get_puuid_matches(puuid)
				average = AverageProcessor.get_rank_average(match_array, puuid)
				
				await bot_logger.edit_message(f'average for {split_message[1]} is {average}')
