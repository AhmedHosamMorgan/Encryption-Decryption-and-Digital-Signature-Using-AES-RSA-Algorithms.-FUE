#AES Encryption & Decryption

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
def aes_encrypt(key, plaintext):
    iv = b'\x9c>\xa5\xe2\x9a\xe6\xf6z\x1b\x8e\xa1\xd7\x83\xe1G\x92'
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext
def aes_decrypt(key, ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
    return plaintext

# Read the image as bytes
with open("/content/drive/MyDrive/HTVD Dataset /2.jpg", "rb") as f:
    plaintext = f.read()

aes_key = b'\x1a\x56\x23\xae\x12\xaf\x45\x90\xbc\x7d\xef\x3c\x2f\x18\x09\x57'
# Encrypt the image using AES
encrypted_image = aes_encrypt(aes_key, plaintext)
# Save the encrypted image as a file
with open("encrypted_image.png", "wb") as f:
    f.write(encrypted_image)

# Read the encrypted image as bytes
with open("encrypted_image.png", "rb") as f:
    ciphertext = f.read()

# Decrypt the image using AES
decrypted_image = aes_decrypt(aes_key, ciphertext)
# Save the decrypted image as a file
with open("decrypted_image.jpg", "wb") as f:
    f.write(decrypted_image)


