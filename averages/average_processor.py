import logging
from utilities.utility_tools import UtilityTools

class AverageProcessor:
    @staticmethod
    def get_rank_average(match_array, puuid):
        query_count = 0
        rank_count = 0
        for match_id in match_array:
            logging.info(
                f"getting match data for: {match_id} query number: {str(query_count)}"
            )
            query_count += 1
            rank_count += UtilityTools.get_most_recent_round_data(puuid, match_id)[
                "placement"
            ]

        average = str(rank_count/len(match_array))
        logging.info(f"player average: {average}")
        return average
