from cryptography.fernet import Fernet
import hashlib


class EncryptionController:
    def __init__(self):
        self.f = Fernet(b"9w98hmJ4ROMc0jdDZvc0okdE7zEuctooCOP0aRlsmzA=")

    def encrypt(self, password: str) -> str:
        return self.f.encrypt(password.encode()).decode("utf-8")

    def decrypt(self, encrypted_password: str) -> str:
        return self.f.decrypt(encrypted_password.encode("utf-8")).decode()

    def hash_password(self, password: str) -> str:
        hasher = hashlib.new("sha256")

        # hash the password
        hasher.update(password.encode())

        # Get the hash in string format
        hash = hasher.hexdigest()

        return hash
