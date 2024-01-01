# RSA Encryption & Decryption
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives
 
import hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

with open('text.txt', 'r') as file:
    message = file.read()

message = message.encode('utf-8')


encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open('encrypted.bin', 'wb') as file:
    file.write(encrypted)

with open('encrypted.bin', 'rb') as file:
    encrypted = file.read()


decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


decrypted_message = decrypted.decode('utf-8')

with open('decrypted.txt', 'w') as file:
    file.write(decrypted_message)

