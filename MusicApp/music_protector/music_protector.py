# MusicProtection/MusicApp/music_protector/music_protector.py

from cryptography.fernet import Fernet
import os

# Clé de chiffrement (vous pouvez générer une clé sécurisée et la stocker en toute sécurité)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_music(file_path):
    with open(file_path, 'rb') as file:
        music_content = file.read()
    
    encrypted_content = cipher_suite.encrypt(music_content)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier original : {e}")

def decrypt_music(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()

    decrypted_content = cipher_suite.decrypt(encrypted_content)

    with open(file_path[:-4], 'wb') as decrypted_file:  # Retirer l'extension .enc
        decrypted_file.write(decrypted_content)

     # Supprimer le fichier chiffré (optionnel)
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier chiffré : {e}")