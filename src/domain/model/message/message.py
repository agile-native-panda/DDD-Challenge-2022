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
        self.id = id
        self.body = body
        self.planned_datetime = planned_datetime
        self.is_reserved_message = is_reserved_message
        self.is_sent_message = False
