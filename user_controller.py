import string
from database_controller import DatabaseController
from encryption_controller import EncryptionController


class UserController:
    def __init__(self) -> None:
        self.ec = EncryptionController()
        self.dc = DatabaseController()

    def login(self, username, password):
        if not self.dc.user_already_exists(username, password):
            raise ValueError("Incorrect Login Details")

        self.set_user_details(username, password)

    def register(self, username, password):
        if not self._is_valid_password(password):
            raise ValueError(
                "Password must at least 8 characters long and include: at least 1 of each:\nLower case character\nUpper case character\nNumber\nSpecial character"
            )

        if self.dc.user_already_exists(username, password):
            raise ValueError("User Already Exists")

        self.dc.add_new_user(username, password)
        self.set_user_details(username, password)

    def set_user_details(self, username, password):
        self.username = username
        self.password = password

    def get_user_accounts(self):
        return self.dc.get_user_acounts(self.username, self.password)

    def add_new_account_to_user(self, platform, email, account_password):
        self.dc.add_new_account_to_user(
            self.username, self.password, platform, email, account_password
        )

    def _is_valid_password(self, password):
        return all(
            [
                any([x in string.ascii_lowercase for x in password]),
                any([x in string.ascii_uppercase for x in password]),
                any([x in string.punctuation for x in password]),
                any([x in string.digits for x in password]),
                len(password) >= 8,
            ]
        )
