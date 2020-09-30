import random
import giphy_client
from giphy_client.rest import ApiException
from config import GIPHY_TOKEN

class JIFFY:

    @staticmethod
    async def get_random_giphy(query):
        api_instance = giphy_client.DefaultApi()

        try:
            response = api_instance.gifs_search_get(GIPHY_TOKEN, 
                query, limit=30)
            lst = list(response.data)
            gif = random.choices(lst)

            return gif[0].url

        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e