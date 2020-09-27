import time
import requests
import logging
from config import API_KEY, TFT_VERSION_COMPARE


class UtilityTools:
    @staticmethod
    def get_puuid(summonerName):
        logging.info("getting player data for: " + summonerName)
        URL = (
            "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"
            + summonerName
            + "?api_key="
            + API_KEY
        )
        response = requests.get(URL)
        puuid = response.json()["puuid"]
        return puuid

    @staticmethod
    def get_puuid_matches(puuid: str) -> None:
        logging.info("getting matches for: " + puuid)
        URL = (
            "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"
            + puuid
            + "/ids?count=5"
            + "&api_key="
            + API_KEY
        )
        response = requests.get(URL)
        match_array = response.json()
        logging.info("Player has played: " + str(len(match_array)))
        logging.info("most recent game id: " + match_array[0])

        return match_array

    @staticmethod
    def get_most_recent_round_data(puuid, match_id: str) -> None:
        URL = (
            "https://americas.api.riotgames.com/tft/match/v1/matches/"
            + match_id
            + "?api_key="
            + API_KEY
        )
        response = requests.get(URL)
        time.sleep(1)
        game_version = str(response.json()["info"]["game_version"])
        print(game_version)
        game_version = float(game_version.split("/")[2].replace(">", ""))

        is_set_4 = game_version >= 10.19
        logging.info(f'Game is in set: {"4" if is_set_4 else "not 4"}')

        participant_index = response.json()["metadata"]["participants"].index(puuid)
        player_data_in_game = response.json()["info"]["participants"][participant_index]
        logging.info(response)
        return player_data_in_game if game_version >= TFT_VERSION_COMPARE else {}
