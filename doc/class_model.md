```mermaid
classDiagram
class User {
    Name name
    Email email
}
class Chat {
    str name
}

class Message {
    Body body
}
Chat o-- User
Chat o-- Message
User --> Message: Create
```