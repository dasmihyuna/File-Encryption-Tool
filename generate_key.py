from cryptography.fernet import Fernet

def save_key(filename="key.key"):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print("Key saved to", filename)

save_key()
