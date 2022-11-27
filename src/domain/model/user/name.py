import dataclasses


@dataclasses.dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str
    nickname: str
    MIN_LEN: int = 0
    MAX_LEN: int = 1000

    def __init__(self, first_name: str, last_name: str, nickname: str) -> None:
        try:
            if not self.__is_valid_body(first_name):
                raise (
                    ValueError(
                        "First Name must be more than {} and less than {}".format(
                            self.MIN_LEN, self.MAX_LEN
                        )
                    )
                )
            if not self.__is_valid_body(last_name):
                raise (
                    ValueError(
                        "Last Name must be more than {} and less than {}".format(
                            self.MIN_LEN, self.MAX_LEN
                        )
                    )
                )
            if not self.__is_valid_body(nickname):
                raise (
                    ValueError(
                        "Nickname must be more than {} and less than {}".format(
                            self.MIN_LEN, self.MAX_LEN
                        )
                    )
                )
            object.__setattr__(self, "first_name", first_name)
            object.__setattr__(self, "last_name", last_name)
            object.__setattr__(self, "nickname", nickname)
        except ValueError as e:
            print(str(e))

    def __is_valid_body(self, body: str) -> bool:
        len_body: int = len(body)

        if self.MIN_LEN < len_body < self.MAX_LEN:
            return True

        return False
