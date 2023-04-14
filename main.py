class PasswordInvalidError(Exception):
    pass


class PasswordLengthError(PasswordInvalidError):
    pass


class PasswordContainUpperError(PasswordInvalidError):
    pass


class PasswordContainDigitError(PasswordInvalidError):
    pass


class User:
    def __init__(self, username, password=None):
        self.username, self.password = username, password

    def set_password(self, newpassword):
        if len(newpassword) < 8:
            raise PasswordLengthError('Пароль должен быть не менее 8 символов')
        if not any(a.isupper() for a in newpassword):
            raise PasswordContainUpperError('Пароль должен содержать хотя бы одну заглавную букву')
        if not any(a.isdigit() for a in newpassword):
            raise PasswordContainDigitError('Пароль должен содержать хотя бы одну цифру')
        self.password = newpassword


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'
