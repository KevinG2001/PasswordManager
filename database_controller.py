from encryption_controller import EncryptionController
from typing import Dict
from copy import deepcopy
import json


class DatabaseController:
    data: Dict[str, dict]
    ec: EncryptionController
    file_path = "data.json"

    def __init__(self) -> None:
        self.ec = EncryptionController()
        self.data = self.read_data_from_file()

    def save_data_to_file(self):
        # Write JSON data to the file
        with open(self.file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def read_data_from_file(self) -> Dict[str, dict]:
        try:
            with open(self.file_path, "r") as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        return data

    def add_new_user(self, username, password):
        hashed_password = self.ec.hash_password(password)
        self.data[username + hashed_password] = dict()

        self.save_data_to_file()

    def add_new_account_to_user(
        self, username, password, platform, email, account_password
    ) -> dict:
        key = username + self.ec.hash_password(password)
        self.data[key][platform] = {
            "email": email,
            "password": self.ec.encrypt(account_password),
        }

        self.save_data_to_file()

        return self.data[key]

    def get_user_acounts(self, username, password) -> dict:
        user_key = username + self.ec.hash_password(password)
        acounts = deepcopy(self.data[user_key])

        for platform in acounts:
            acounts[platform]["password"] = self.ec.decrypt(
                acounts[platform]["password"]
            )

        return acounts

    def user_already_exists(self, username, password) -> bool:
        key = username + self.ec.hash_password(password)
        return self.data.get(key) is not None
