from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted = file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print("Wrong key or corrupted file.")
        return

    output_file = file_path.replace(".enc", ".dec")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"Decrypted and saved as {output_file}")

decrypt_file("secret.txt.enc")
