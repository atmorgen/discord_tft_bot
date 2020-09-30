import logging
from items.item_processor import ItemProcessor
from averages.average_processor import AverageProcessor
from utilities.utility_tools import UtilityTools
from logger.bot_logger import BotLogger

class TFTDiscordBot:            

    @staticmethod
    async def process_message(message):
        print(message.author)
        bot_logger = BotLogger(message)
        if message.content.lower() == "do a barrel roll!":
            await bot_logger.do_a_barrel_roll()
            return

        if str(message.channel) == "tft_bot_channel":
            if message.content == "Slave Bot, Say Hello":
                await bot_logger.send_message("Hello!")

            split_message = message.content.split(" ")

            if split_message[0].upper() == "TFT:":
				
                if len(split_message) != 3:
                    await bot_logger.send_message("Your message doesn't make sense")
                    return
                
                puuid = await UtilityTools.get_puuid(split_message[1])
                
                success_response = (
                    f"processing average for {split_message[1]} over {split_message[2]} "
                    + "games. this will take a bit (about 1 second per game, cause riot)"
                )
                
                fail_response = f"No player named: {split_message[1]} found"
                
                processing_message = await bot_logger.send_message(
                        success_response if puuid != None else fail_response
                    )

                bot_logger.set_message(
                    processing_message
                )

                match_array = await UtilityTools.get_puuid_matches(puuid, split_message[2], bot_logger)
                
                if len(match_array) == 0:
                    await bot_logger.edit_message(
                        f"{split_message[1]} has no matches"
                    )
                    return

                await AverageProcessor.get_rank_average(split_message[1], split_message[2], match_array, puuid, bot_logger)
