from src.domain.model.user.email import Email
from faker import Faker
import pytest
from email_validator import EmailNotValidError


fake = Faker("ja_jp")


class TestEmail:
    def test_create_instance(self):
        email_body = fake.email()
        email = Email(email_body)
        assert email.body == email_body

    def test_create_instance_wrong_body(self, capfd):
        email_body = "aaaaa"
        email = Email(email_body)
        out, err = capfd.readouterr()
        assert (
            out == "The email address is not valid. It must have exactly one @-sign.\n"
        )
        assert err is ""
