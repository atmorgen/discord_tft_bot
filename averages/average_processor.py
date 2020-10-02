import logging
from utilities.utility_tools import UtilityTools

class AverageProcessor:
    @staticmethod
    async def get_rank_average(name, num_games, match_array, puuid, bot_logger):
        query_count = 0
        ranked_games_count = 0
        ranked_placement_count = 0
        unranked_games_count = 0
        unranked_placement_count = 0
        for match_id in match_array:
            logging.info(
                f"getting match data for: {match_id} query number: {str(query_count)}"
            )
            query_count += 1
            round_data = await UtilityTools.get_most_recent_round_data(puuid, match_id, bot_logger)
            match_data = UtilityTools.get_player_data_in_game(round_data, puuid)

            #unranked
            queue_id = round_data["info"]["queue_id"]
            if queue_id == 1090:
                unranked_games_count += 1
                unranked_placement_count += match_data[
                    "placement"
                ]
            #ranked
            else:
                ranked_games_count += 1
                ranked_placement_count += match_data[
                    "placement"
                ]

        unranked_average = 0 if unranked_games_count==0 else str(round(unranked_placement_count/unranked_games_count,2))
        ranked_average = 0 if ranked_games_count==0 else str(round(ranked_placement_count/ranked_games_count,2))
        
        logging.info(f'done processing average for {name}')

        await bot_logger.edit_message(
            f"""Averages for `{name}`:
            Unranked: average over `{unranked_games_count}` games is `{unranked_average}`
            Ranked: average over `{ranked_games_count}` games is `{ranked_average}`
            """
        )

