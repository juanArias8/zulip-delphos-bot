import re
from datetime import datetime
from typing import List

from src.models.schemas import Message


def format_messages(messages: List[Message]) -> List[str]:
    all_items = []

    for message in messages:
        cleaned = remove_delphos_messages(message.content, message.sender_email)
        cleaned = remove_quotes(cleaned)
        cleaned = remove_mentions(cleaned)

        if cleaned:
            all_items.append(
                f"{datetime.fromtimestamp(message.timestamp)} "
                f"{message.sender_full_name}: {cleaned}"
            )

    return all_items


def remove_delphos_messages(message: str, sender_email: str) -> str:
    is_delphos_sender = sender_email == "delphos-bot@zulip.monadical.com"
    is_delphos_message = message.startswith("@**Delphos**")
    if is_delphos_sender or is_delphos_message:
        return ""
    return message


def remove_quotes(message: str) -> str:
    if "** [said](" in message:
        message = re.sub(r"@_\*\*(.*?)\):", "", message)
        message = re.sub(r"```quote\n(.*?)\n```", "", message)
        message = re.sub(r"^\s+|\s+$", "", message)
    return message


def remove_mentions(message: str) -> str:
    return message.replace("**", "")
