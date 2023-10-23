import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
from src.lab2.rsa import generate_keypair, encrypt, decrypt


class CipherTestCase(unittest.TestCase):

    def test_caesar(self):
        message = "Aboba"
        shift = 25
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted)
        self.assertEquals(encrypted, "Zanaz")
        self.assertEquals(decrypted, message)

        message = "Raiden"
        shift = 11
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted)
        self.assertEquals(encrypted, "Cltopy")
        self.assertEquals(decrypted, message)

        message = "BIGLETTERS"
        shift = 2
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted)
        self.assertEquals(encrypted, "DKINGVVGTU")
        self.assertEquals(decrypted, message)

        message = "smol"
        shift = 6
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted)
        self.assertEquals(encrypted, "ysur")
        self.assertEquals(decrypted, message)

        message = ""
        shift = 1000000000000
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted)
        self.assertEquals(encrypted, "")
        self.assertEquals(decrypted, message)

    def test_vigenere(self):
        message = "Biba"
        key = "Boba"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted)
        self.assertEquals(encrypted, "Dxdb")
        self.assertEquals(decrypted, message)

        message = "Raiden"
        key = "Yae"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted)
        self.assertEquals(encrypted, "Qbncfs")
        self.assertEquals(decrypted, message)

        message = "AAAAA"
        key = "B"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted)
        self.assertEquals(encrypted, "CCCCC")
        self.assertEquals(decrypted, message)

        message = "smol"
        key = "letters"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted)
        self.assertEquals(encrypted, "erif")
        self.assertEquals(decrypted, message)

        message = ""
        key = "AmaWannaCheeseBueger"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted)
        self.assertEquals(encrypted, "")
        self.assertEquals(decrypted, message)

    def test_rsa(self):
        message = "Biba"
        p, q = 443, 709
        public, private = generate_keypair(p, q)
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)
        self.assertEquals(decrypted, message)

        message = "Raiden"
        p, q = 79, 337
        public, private = generate_keypair(p, q)
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)
        self.assertEquals(decrypted, message)

        message = "BIG"
        p, q = 227, 601
        public, private = generate_keypair(p, q)
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)
        self.assertEquals(decrypted, message)

        message = "notbig"
        p, q = 191, 1109
        public, private = generate_keypair(p, q)
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)
        self.assertEquals(decrypted, message)

        message = ""
        p, q = 443, 709
        public, private = generate_keypair(p, q)
        encrypted = encrypt(private, message)
        decrypted = decrypt(public, encrypted)
        self.assertEquals(decrypted, message)