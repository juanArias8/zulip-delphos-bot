from typing import Optional, Protocol, List

from src.models.schemas import Command


class BaseOperator(Protocol):

    def get_response(self, commands: Optional[Command]) -> List[str]:
        ...
