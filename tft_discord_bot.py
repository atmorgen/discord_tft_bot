import logging
from items.item_processor import ItemProcessor
from averages.average_processor import AverageProcessor
from utilities.utility_tools import UtilityTools
from logger.bot_logger import BotLogger


class TFTDiscordBot:
    @staticmethod
    async def process_message(message):

        bot_logger = BotLogger(message)

        if str(message.channel) == "tft_bot_channel":
            if message.content == "Slave Bot, Say Hello":
                await bot_logger.send_message("Hello!")

            split_message = message.content.split(" ")
            if len(split_message) != 3:
                await bot_logger.send_message("Your message doesn't make sense")
                return
            if split_message[0].upper() == "TFT:":
                puuid = UtilityTools.get_puuid(split_message[1])
                success_response = (
                    f"processing average for {split_message[1]} over {split_message[2]} "
                    + "games. this will take a bit (about 1 second per game, cause riot)"
                )
                fail_response = f"No player named: {split_message[1]} found"
                print(puuid != None)
                bot_logger.set_message(
                    await bot_logger.send_message(
                        success_response if puuid != None else fail_response
                    )
                )

                match_array = UtilityTools.get_puuid_matches(puuid, split_message[2])
                average = AverageProcessor.get_rank_average(match_array, puuid)

                await bot_logger.edit_message(
                    f"average for {split_message[1]} over the last {split_message[2]} games is {average}"
                )