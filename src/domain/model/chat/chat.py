from ..message import Message
from ..user import User
import uuid


class Chat:
    id: uuid.UUID
    name: str
    message_list: list[Message]
    user_list: list[User]
    NAME_MAX_LEN: int = 100

    def __init__(self, id: uuid.UUID, name: str, user_list: list[User]) -> None:
        if not self.__is_valid_name(name):
            raise (
                ValueError("Chat name must be less than {}".format(self.NAME_MAX_LEN))
            )
        self.id = id
        self.name = name
        self.message_list = []
        self.user_list = user_list

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Chat):
            return self.id == object.id
        return False

    def __is_valid_name(self, name: str):
        len_name = len(name)
        if len_name <= self.NAME_MAX_LEN:
            return True
        return False
