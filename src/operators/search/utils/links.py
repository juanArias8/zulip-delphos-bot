import math
import re
from typing import Union, List

from src.models.schemas import Message


def format_links(messages: List[Message]) -> List[str]:
    amount = 10
    all_items = []
    for message in messages:
        all_items.extend(extract_links_from_string(message.content))

    unique_items = list(set(all_items))
    sliced_list = [
        format_links_response(unique_items[i * amount: (i + 1) * amount])
        for i in range(math.ceil(len(unique_items) / amount))
    ]
    return sliced_list


def extract_links_from_string(input_string: str) -> Union[List[str], None]:
    regex = re.compile(r'href=[\'"]?(http[^\'" >]+)', re.I)
    match = regex.findall(input_string)
    return match


def format_links_response(links: List[str]):
    return '\n'.join(f"[]({link})" for link in links)
