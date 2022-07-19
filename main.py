from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        lst=number.split('-')
        print(lst)


    @staticmethod
    def check_name(name: str) -> bool:
        pass


print(CardCheck.check_card_number("1234-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))
