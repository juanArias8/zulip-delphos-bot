from typing import List

from src.utils.constants import HELP_MESSAGE

from src.models.schemas import Command


class HelpOperator:
    @staticmethod
    def get_response(command: Command) -> List[str]:
        return [HELP_MESSAGE]
