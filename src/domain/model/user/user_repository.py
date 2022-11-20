from abc import ABC, abstractmethod
from typing import List, Optional
from . import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> None:
        return

    @abstractmethod
    def save(self) -> Nore:
        return
