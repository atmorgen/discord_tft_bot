import requests
import json
import time
from items.item_processor import ItemProcessor
from utilities.utility_tools import UtilityTools
from averages.average_processor import AverageProcessor
from config import API_KEY

query_count = 0

class TFTDiscordBot:

	puuid = None
	match_array = None

	def __init__(self):
		print("starting up discord tft bot")
		self.puuid = UtilityTools.get_puuid()
		self.match_array = UtilityTools.get_puuid_matches(self.puuid)
		self.start_up()

	def start_up(self):
		#AverageProcessor.get_rank_average(match_array, puuid)
		ItemProcessor.get_item_average(self.match_array, self.puuid)
