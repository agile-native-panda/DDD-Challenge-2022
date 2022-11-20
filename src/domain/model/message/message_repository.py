from abc import ABC, abstractmethod
from . import Message
from ..chat import Chat
from ..user import User


class MessageRepository(ABC):
    @abstractmethod
    def create(self, message: Message) -> None:
        return

    @abstractmethod
    def update(self, messsage: Message) -> None:
        return

    @abstractmethod
    def delete(self, messsage: Message) -> None:
        return

    @abstractmethod
    def get_message_list_in_chat(self, chat: Chat) -> list[Chat]:
        return

    @abstractmethod
    def get_message_list_in_user(self, user: User) -> list[Message]:
        return
