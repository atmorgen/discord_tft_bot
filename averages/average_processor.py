import logging
from utilities.utility_tools import UtilityTools
from logger.traits_object import TraitsObject

class AverageProcessor:
    @staticmethod
    async def get_rank_average(name, num_games, match_array, puuid, bot_logger):
        query_count = 0
        ranked_games_count = 0
        ranked_placement_count = 0
        unranked_games_count = 0
        unranked_placement_count = 0

        players_eliminated = 0
        gold_left = 0
        total_damage_to_players = 0

        traits_object = TraitsObject()
        for match_id in match_array:
            logging.info(
                f"getting match data for: {match_id} query number: {str(query_count)}"
            )
            round_data = await UtilityTools.get_most_recent_round_data(puuid, match_id, bot_logger)
            match_data = UtilityTools.get_player_data_in_game(round_data, puuid)

            game_version = round_data["info"]["tft_set_number"]

            if game_version != 4:
                logging.info('Game is in not in set 4...ignoring')
                break
            
            query_count += 1
            logging.info('Game is in set 4')

            traits_object.process_traits(match_data['traits'])

            players_eliminated += match_data["players_eliminated"]
            gold_left += match_data["gold_left"]
            total_damage_to_players += match_data["total_damage_to_players"]
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
        
        total_games = ranked_games_count + unranked_games_count

        players_eliminated_average = str(round(players_eliminated/total_games,2))
        gold_left_average = str(round(gold_left/total_games,2))
        total_damage_to_players_average = str(round(total_damage_to_players/total_games,2))

        traits_object.set_averages(ranked_games_count+unranked_games_count)

        logging.info(f'done processing average for {name}')

        await bot_logger.edit_message(
            f"""Averages for `{name}`:
            Total of `{query_count}` games in Set 4
            Unranked: average over `{unranked_games_count}` games is `{unranked_average}`
            Ranked: average over `{ranked_games_count}` games is `{ranked_average}`
            Players Eliminated: `{players_eliminated_average}`
            Gold Left: `{gold_left_average}`
            Damage to players: `{total_damage_to_players_average}`

            {traits_object.to_string()}
            """
        )

