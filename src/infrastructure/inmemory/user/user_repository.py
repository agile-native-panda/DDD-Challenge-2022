from src.domain.model.user import UserRepository, User


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.store: list[User] = []

    def create(self, user: User) -> None:
        # TODO: ここにemailの確認
        self.save(user)

    def save(self, user: User) -> None:
        self.store += user
