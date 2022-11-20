class Body:
    text: str
    MAX_LEN: int = 1000

    def __init__(self, text: str) -> None:
        try:
            if not self.__is_valid_text(text):
                raise (ValueError("Text must be less than {}".format(self.MAX_LEN)))
            self.text = text
        except ValueError as e:
            print(str(e))

    def __is_valid_text(self, text: str) -> bool:
        len_text: int = len(text)
        if len_text <= self.MAX_LEN:
            return True
        return False
