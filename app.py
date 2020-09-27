import logging
from tft_discord_bot import TFTDiscordBot

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)
def main():
    TFTDiscordBot()

if __name__ == "__main__":
    main()