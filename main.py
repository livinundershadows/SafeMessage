import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class generate_keys:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        self.public_key = self.private_key.public_key()

        pemPrivate = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open('private_key.pem', 'wb') as f:
            f.write(pemPrivate)
            f.close()

        pemPublic = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open('public_key.pem', 'wb') as f:
            f.write(pemPublic)
            f.close()

    def open_encry_file(self, file_path):
        with open(file_path, 'r') as f:
            self.message = bytes(f.read(), encoding='utf-8')
            f.close()

    def encrypt_txt(self, new_name):
        encrypted = self.public_key.encrypt(
            self.message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open(new_name, 'wb') as f:
            f.write(encrypted)
            f.close()

    def decrypt_txt(self, file_decrypt):
        with open(file_decrypt, 'rb') as f:
            Emessage = f.read()
            f.close()
        original_message = self.private_key.decrypt(
            Emessage,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print(original_message)






