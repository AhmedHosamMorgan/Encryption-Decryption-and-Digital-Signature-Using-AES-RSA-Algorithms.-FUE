# RSA Digital Signatures and Hashing
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a new RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

message = b"This is the message to be signed."

# Create a new SHA256 object and update it with the message
hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
hasher.update(message)

# Get the digest of the message
digest = hasher.finalize()

# Sign the digest with the private key
signature = private_key.sign(
    digest,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Verify the signature with the public key against the digest
try:
    public_key.verify(
        signature,
        digest,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("The signature is valid.")
except cryptography.exceptions.InvalidSignature:
    print("The signature is invalid.")

