import dataclasses
from email_validator import validate_email, EmailNotValidError

@dataclasses.dataclass(frozen=True)
class Email:
    body: str
    def __init__(self, body: str) -> None:
        try:
            validation = validate_email(body, check_deliverability=True)
            self.body = validation.email
        except EmailNotValidError as e:
            print(str(e))