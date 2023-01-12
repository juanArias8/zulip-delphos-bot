from types import ModuleType
from typing import Any, Dict, Optional

from pydantic import BaseModel
from zulip_bots.lib import ExternalBotHandler


class Settings(BaseModel):
    bots_lib_modules: Optional[Dict[str, ModuleType]]
    bot_handlers: Optional[Dict[str, ExternalBotHandler]]
    message_handlers: Optional[Dict[str, Any]]

    class Config:
        arbitrary_types_allowed = True
