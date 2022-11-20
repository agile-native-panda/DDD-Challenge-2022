from ..message import Message
from ..user import User


class Chat:
    name: str
    message_list: list[Message]
    user_list: list[User]
    NAME_MIN_LEN: int = 0
    NAME_MAX_LEN: int = 100

    def __init__(self, name: str, user_list: list[User]) -> None:
        if not self.__is_valid_name(name):
            raise (
                ValueError("Chat name must be more than {} and less than {}".format(self.NAME_MIN_LEN, self.NAME_MAX_LEN))
            )
        self.name = name
        self.message_list = []
        self.user_list = user_list

    def __is_valid_name(self, name: str):
        len_name = len(name)
        if self.NAME_MIN_LEN < len_name < self.NAME_MAX_LEN:
            return True
        return False
