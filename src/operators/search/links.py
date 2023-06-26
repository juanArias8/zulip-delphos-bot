from typing import List

from src.integrations.zulip_integration import ZulipIntegration
from src.models.schemas import Command
from src.operators.search.utils.links import format_links
from src.utils.constants import LINKS_HELP


class LinksOperator:
    def __init__(self):
        self.zulip_integration = ZulipIntegration()

    def get_response(self, command: Command) -> List[str]:
        print(command)
        if len(command.params) == 2:
            command.stream = command.params[0]
            command.topic = command.params[1]

        print(command)
        if not (command.stream and command.topic):
            return [LINKS_HELP]

        return self.search_links(stream=command.stream, topic=command.topic)

    def search_links(self, *, stream: str, topic: str) -> List[str]:
        request = self.zulip_integration.build_search_narrow(
            stream=stream,
            topic=topic,
            content="link",
        )
        response = self.zulip_integration.get_zulip_messages(request)
        if response.result == "success":
            return format_links(response.messages)
        return [f"Error searching links in Zulip: {response.msg}"]
