from src.domain.model.message import Message, MessageRepository


class InMemoryMessageRepository(MessageRepository):
    def __init__(self) -> None:
        self.store: list[Message] = []

    def create(self, message: Message) -> None:
        self.save(message)

    def save(self, message: Message) -> None:
        self.store += message
