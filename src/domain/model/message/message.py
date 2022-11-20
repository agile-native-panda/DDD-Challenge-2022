import datetime
from . import Body


class Message:
    body: Body
    planned_datetime: datetime.datetime
    is_reserved_message: bool
    is_sent_message: bool

    def __init__(
        self, body: Body, planned_datetime: datetime.datetime, is_reserved_message: bool
    ) -> None:
        self.body = body
        self.planned_datetime = planned_datetime
        self.is_reserved_message = is_reserved_message
        self.is_sent_message = False
