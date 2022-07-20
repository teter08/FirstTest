from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        return (all(map(lambda x: set(x) <= set(digits), number.split('-'))) and number[4] == number[9] == number[
            14] == '-' and len(number) == 19)

    @classmethod
    def check_name(cls, name: str) -> bool:
        return (all(map(lambda x: set(x) <= set(cls.CHARS_FOR_NAME), name.split())) and len(name.split()) == 2)


print(CardCheck.check_card_number("1234-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))
