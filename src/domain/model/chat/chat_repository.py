from abc import ABC, abstractmethod
from . import Message
from ..chat import Chat
from ..user import User


class MessageRepository(ABC):
    @abstractmethod
    def create(self, chat: Chat) -> None:
        return

    @abstractmethod
    def update(self, chat: Chat) -> None:
        return
