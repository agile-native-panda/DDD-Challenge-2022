import datetime
from . import Body
import uuid


class Message:
    body: Body
    id: uuid.UUID
    planned_datetime: datetime.datetime
    is_reserved_message: bool
    is_sent_message: bool

    def __init__(
        self,
        id: uuid.UUID,
        body: Body,
        planned_datetime: datetime.datetime,
        is_reserved_message: bool,
    ) -> None:
        if not self.__is_valid_planned_datetime(planned_datetime):
            raise (
                    ValueError("Planned datetime must be later than now")
            )
        self.id = id
        self.body = body
        self.planned_datetime = planned_datetime
        self.is_reserved_message = is_reserved_message
        self.is_sent_message = False

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Message):
            return self.id == object.id
        return False

    def __is_valid_planned_datetime(self, planned_datetime: datetime.datetime) -> bool:
        if datetime.datetime.now() < planned_datetime:
            return True
        return False