from src.domain.model.user import UserRepository, User, Email
from src.domain.service import UserService
from typing import Optional


class InMemoryUserRepository(UserRepository):
    user_service = UserService()

    def __init__(self) -> None:
        self.store: list[User] = []

    def create(self, user: User) -> None:
        if self.user_service.is_duplicated(user):
            raise ValueError("This email is already used.")
        else:
            self.save(user)

    def save(self, user: User) -> None:
        self.store += user

    def get_user_by_email(self, email: Email) -> Optional[User]:
        for user in self.store:
            if email == user.email:
                return user
        return None
