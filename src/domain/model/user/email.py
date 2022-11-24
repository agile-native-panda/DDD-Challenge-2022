import dataclasses
from email_validator import validate_email, EmailNotValidError


@dataclasses.dataclass(frozen=True, init=False)
class Email:
    body: str

    def __init__(self, body: str) -> None:
        try:
            validation = validate_email(body, check_deliverability=False)
            object.__setattr__(self, "body", validation.email)
        except EmailNotValidError as e:
            print(str(e))

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Email):
            return self.body == object.body
        return False
