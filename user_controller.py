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
