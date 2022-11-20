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

    def create_chat(self) -> None:
        chat = Chat()
        self.chat_list.append(chat)
    
    def update_chat(self) -> None:
        pass
    
    def create_message(self):
        pass
    
    def update_reserved_message(self):
        pass
    
    def delete_reserved_message(self):
        pass
    
    def get_reserved_message_list(self):
        pass