import asyncio
import requests
import logging
from constants import OK, RATE_LIMIT
from config import API_KEY, TFT_VERSION_COMPARE


class UtilityTools:
    @staticmethod
    async def get_puuid(summonerName):
        logging.info("getting player data for: " + summonerName)
        URL = (
            "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"
            + summonerName
            + "?api_key="
            + API_KEY
        )
        response = requests.get(URL)
        puuid = response.json().get("puuid", {})

        return puuid if response.status_code == OK else None

    @staticmethod
    async def get_puuid_matches(puuid: str, count: str, bot_logger) -> None:
        logging.info("getting matches for: " + puuid)
        URL = (
            "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"
            + puuid
            + "/ids?count="
            + count
            + "&api_key="
            + API_KEY
        )
        response = requests.get(URL)

        if await UtilityTools.check_rate_limit(response.status_code, bot_logger):
            return {}
        match_array = response.json()
        logging.info("Player has played: " + str(len(match_array)))
        if len(match_array) > 0:
            logging.info("most recent game id: " + match_array[0])
        else:
            logging.info("player has no matches")
        return match_array

    @staticmethod
    async def get_most_recent_round_data(puuid, match_id: str, bot_logger) -> None:
        URL = (
            "https://americas.api.riotgames.com/tft/match/v1/matches/"
            + match_id
            + "?api_key="
            + API_KEY
        )
        await asyncio.sleep(1)
        response = requests.get(URL)
        if await UtilityTools.check_rate_limit(response.status_code, bot_logger):
            return {"placement": 4}

        return response.json()

    @staticmethod
    def get_player_data_in_game(round_data, puuid):
        participant_index = round_data["metadata"]["participants"].index(puuid)
        return round_data["info"]["participants"][participant_index]


    @staticmethod
    async def check_rate_limit(status, bot_logger):
        if status == RATE_LIMIT:
            logging.info("RATE LIMIT EXCEEDED")
            await bot_logger.i_broke_cause_rate_limit()
        return status == RATE_LIMIT
