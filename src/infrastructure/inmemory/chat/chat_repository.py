from src.domain.model.chat import ChatRepository, Chat


class InMemoryChatRepository(ChatRepository):
    def __init__(self) -> None:
        self.store: list[Chat] = []

    def create(self, chat: Chat) -> None:
        self.save(chat)

    def save(self, chat: Chat) -> None:
        self.store += chat
