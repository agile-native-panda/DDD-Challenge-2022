import dataclasses

@dataclasses.dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str
    nickname: str
    MAX_LEN: int = 1000

    def __init__(self, first_name: str, last_name: str, nickname:str) -> None:
        try: 
            if not self.__is_valid_body(first_name) :
                raise(ValueError("First Name must be less than {}".format(self.MAX_LEN)))
            if not self.__is_valid_body(first_name) :
                raise(ValueError("Last Name must be less than {}".format(self.MAX_LEN)))
            if not self.__is_valid_body(first_name) :
                raise(ValueError("Nickname must be less than {}".format(self.MAX_LEN)))
            self.first_name = first_name
            self.last_name = last_name
            self.nickname = nickname
        except ValueError as e :
            print(str(e))
        
    def __is_valid_body(self, body: str) -> bool:
        len_body: int = len(body)
        
        if len_body <= self.MAX_LEN:
            return True
        return False