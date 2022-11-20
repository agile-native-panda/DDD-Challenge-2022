from ..model import User, UserRepository


class UserService:
    def IsDuplicated(self, user: User) -> bool:
        user_repository = UserRepository()
        if user_repository.get_user_by_email(user):
            raise ValueError("This email is already exist.")
        else:
            user_repository.create(user)
