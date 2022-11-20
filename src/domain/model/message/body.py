class Body:
    text: str
    MIN_LEN: int = 0
    MAX_LEN: int = 1000

    def __init__(self, text: str) -> None:
        try:
            if not self.__is_valid_text(text):
                raise (
                    ValueError("Text must be more than {} and less than {}".format(self.NAME_MIN_LEN, self.NAME_MAX_LEN))
                )
            self.text = text
        except ValueError as e:
            print(str(e))

    def __is_valid_text(self, text: str) -> bool:
        len_text: int = len(text)
        if self.MIN_LEN < len_text <= self.MAX_LEN:
            return True
        return False
