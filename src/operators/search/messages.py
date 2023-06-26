from typing import List

from src.integrations.zulip_integration import ZulipIntegration
from src.models.schemas import Command
from src.operators.search.utils.messages import format_messages
from src.utils.constants import MESSAGES_HELP


class MessagesOperator:
    def __init__(self):
        self.zulip_integration = ZulipIntegration()

    def get_response(self, command: Command) -> List[str]:
        # From Stream chat => messages 100
        limit = command.params[0] if len(command.params) > 0 else 1000

        # From private chat => messages 100 stream topic
        if len(command.params) == 3:
            command.stream = command.params[1]
            command.topic = command.params[2]

        # Validate command
        if not (command.stream and command.topic):
            return [MESSAGES_HELP]

        return self.search_messages(
            stream=command.stream,
            topic=command.topic,
            limit=limit
        )

    def search_messages(self, *, stream: str, topic: str, limit: int) -> List[str]:
        request = self.zulip_integration.build_search_narrow(
            stream=stream,
            topic=topic,
            limit=limit,
            apply_markdown=False
        )
        response = self.zulip_integration.get_zulip_messages(request)
        if response.result == "success":
            content = format_messages(response.messages)
            file_name = self.zulip_integration.upload_file_to_zulip(
                f"{stream}-{topic}.txt", content
            )
            return [file_name or "Error uploading file to Zulip."]

        return [f"Error searching messages in Zulip: {response.msg}"]
