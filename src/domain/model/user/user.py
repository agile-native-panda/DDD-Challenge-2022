from __future__ import annotations
from ..chat import Chat
from . import Name, Email


class User:
    name: Name
    email: Email
    chat_list: list[Chat]

    def __init__(self, name: Name, email: Email) -> None:
        self.name = name
        self.email = email
        self.chat_list = []

    def __eq__(self, object: object) -> bool:
        if isinstance(object, User):
            return self.email == object.email
        return False
