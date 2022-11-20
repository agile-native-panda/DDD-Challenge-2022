from ..model import User, UserRepository


class UserService:
    def IsDuplicated(self, user: User) -> bool:
        user_repository = UserRepository()
        if user_repository.get_user_by_email(user):
            return True
        else:
            return False
