import logging
from utilities.utility_tools import UtilityTools


class ItemProcessor:
    @staticmethod
    def get_item_average(match_array, puuid):
        total_items = 0
        query_count = 0
        for match_id in match_array:
            logging.info(
                "getting match data for: "
                + match_id
                + " query number: "
                + str(query_count)
            )
            query_count += 1
            total_items += ItemProcessor.count_items(
                UtilityTools.get_most_recent_round_data(puuid, match_id)
            )

        logging.info("average: " + str(total_items / len(match_array)))

    @staticmethod
    def count_items(player_data):
        item_count = 0
        for unit in player_data["units"]:
            for item in unit["items"]:
                item_id = int(item)
                item_count += 2 if item_id > 9 else 1

        return item_count
