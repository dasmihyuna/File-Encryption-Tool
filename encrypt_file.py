from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"Encrypted and saved as {file_path}.enc")

encrypt_file("secret.txt")