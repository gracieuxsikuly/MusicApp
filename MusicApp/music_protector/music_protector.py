# MusicApp/music_protector/__init__.py
# (ce fichier peut rester vide)

# MusicApp/music_protector/music_protector.py

from cryptography.fernet import Fernet
import os

class MusicProtector:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        return key

    def encrypt_music(self, input_file, output_file):
        with open(input_file, 'rb') as music_file:
            music_data = music_file.read()

        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(music_data)

        with open(output_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

    def decrypt_music(self, input_file, output_file):
        with open(input_file, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        cipher_suite = Fernet(self.key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        with open(output_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
