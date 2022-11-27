from src.domain.model.user.name import Name
from faker import Faker
import pytest

fake = Faker("ja-jp")


class TestName:
    def test_create_instace(self):
        first_name = fake.first_name()
        last_name = fake.last_name()
        nickname = fake.name()
        name = Name(first_name=first_name, last_name=last_name, nickname=nickname)
        assert name.first_name == first_name
        assert name.last_name == last_name
        assert name.nickname == nickname

    def test_create_instance_invalid_body(self, capfd):
        first_name = "a"
        last_name = ""
        nickname = ""
        name = Name(first_name=first_name, last_name=last_name, nickname=nickname)
        # print(name.last_name)
        out, err = capfd.readouterr()
        assert out == "Last Name must be more than 0 and less than 1000\n"
        assert err is ""
