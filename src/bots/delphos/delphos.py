from typing import Any, Dict

import requests
from zulip_bots.lib import BotHandler


def get_weather(city_name: str):
    API_KEY = "37bf4285515446549a4222213231001"
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"
    return requests.get(url).json()


class DelphosHandler:
    ERROR_MESSAGE = """
    Sorry, No command/city found. You need to write the command and city: 
    '@weather weather <city>' or 'weather <city>' in DM
    """

    def usage(self) -> str:
        return """
        This is a weather report system,
        Please specify the city name to obtain detailed info.
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        content = message.get("content", None)
        response = self.ERROR_MESSAGE

        try:
            content = content.strip().split()[-2:]
            command = content[0]
            city = content[1]
        except IndexError as e:
            command = None
            city = None

        if command == "weather" and city:
            response = get_weather(city)

        bot_handler.send_reply(message, response)
        return


handler_class = DelphosHandler
