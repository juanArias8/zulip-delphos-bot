from typing import List, Any, Union

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    sender_id: int
    content: str
    recipient_id: int
    timestamp: int
    client: str
    is_me_message: bool
    sender_full_name: str
    sender_email: str
    sender_realm_str: str
    subject: str = None
    topic_links: List[Any] = None
    last_edit_timestamp: int = None
    edit_history: Any = None
    reactions: List[Any] = None
    submessages: List[Any] = None
    flags: List[str] = None
    display_recipient: Union[Any, str] = None
    type: str = None
    stream_id: int = None
    avatar_url: str = None
    content_type: str = None
    rendered_content: str = None


class ZulipEvent(BaseModel):
    data: str
    message: Message
    bot_email: str
    trigger: str
    token: str
    bot_full_name: str
