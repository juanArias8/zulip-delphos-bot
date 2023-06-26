import shlex
from typing import Any, Dict

from zulip_bots.lib import BotHandler

from src.models.schemas import Command, Instruction
from src.operators.base import BaseOperator
from src.operators.help import HelpOperator
from src.operators.search.links import LinksOperator
from src.operators.search.messages import MessagesOperator
from src.utils.constants import ERROR_HELP


class DelphosHandler:
    @staticmethod
    def usage() -> str:
        return """
            Zulip Bot for advanced search
            """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler):
        message_type = message.get("type", None)  # private or stream
        content = message.get("content", None)  # message content

        if not (message_type and content):
            return [ERROR_HELP]

        # splits the content ["@Delphos", "messages", "10"]
        content = shlex.split(content.strip())
        if len(content) == 0:
            return [ERROR_HELP]

        mentions = ["Delphos", "@**Delphos**"]
        starts_with_mention = content[0] in mentions
        if message_type == "private" and starts_with_mention:
            content = content[1:]

        command = Command(instruction=content[0], params=content[1:])
        if message_type == "stream":
            command.stream = message.get("display_recipient", None)
            command.topic = message.get("subject", None)

        instance = self.get_operator_instance(command)
        response = instance.get_response(command)

        for item in response:
            bot_handler.send_reply(message, item)

    @staticmethod
    def get_operator_instance(command: Command) -> BaseOperator:
        instructions = Instruction
        available_operators = {
            instructions.HELP: HelpOperator,
            instructions.MESSAGES: MessagesOperator,
            instructions.LINKS: LinksOperator,
        }
        operator_class = available_operators.get(command.instruction)
        return HelpOperator() if operator_class is None else operator_class()


handler_class = DelphosHandler
