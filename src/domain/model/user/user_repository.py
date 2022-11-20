from abc import ABC, abstractmethod
from typing import List, Optional
from . import User, Email
from typing import Optional


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> None:
        return

    @abstractmethod
    def save(self, user: User) -> None:
        return

    @abstractmethod
    def get_user_by_email(self, email: Email) -> Optional[User]:
        return
