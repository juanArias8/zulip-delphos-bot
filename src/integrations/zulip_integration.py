import io
from typing import List, Union, Any, Dict

from zulip import Client

from src.models.schemas import ZulipResponse


class ZulipIntegration:
    def __init__(self):
        self.client = Client(config_file="./zuliprc-api")

    def get_zulip_messages(self, request: Any):
        messages = self.client.get_messages(request)
        return ZulipResponse(**messages)

    def upload_file_to_zulip(self, filename: str, content: List[str]) -> Union[str, None]:
        with io.StringIO("\n".join(content)) as fstream:
            fstream.name = filename
            result = self.client.upload_file(fstream)
        uri = result.get("uri")
        return f"[{filename}]({uri})" if uri else None

    @staticmethod
    def build_search_narrow(
            *,
            stream: str,
            topic: str,
            limit: int = 1000,
            content: str = None,
            apply_markdown: bool = True,
    ) -> Dict[str, Any]:
        narrow = {
            "anchor": "newest",
            "num_before": limit,
            "num_after": 0,
            "apply_markdown": apply_markdown,
            "narrow": [
                {"operator": "stream", "operand": stream},
                {"operator": "topic", "operand": topic},
            ],
        }

        if content:
            narrow["narrow"].append({"operator": "has", "operand": content})

        return narrow
