import random
import string
import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
from src.lab2.rsa import generate_keypair, encrypt, decrypt


class CipherTestCase(unittest.TestCase):

    def test_caesar(self):
        message = "Aboba"
        shift = 25
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted, shift)
        self.assertEquals(encrypted, "Zanaz")
        self.assertEquals(decrypted, message)

        message = "Raiden"
        shift = 11
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted, shift)
        self.assertEquals(encrypted, "Cltopy")
        self.assertEquals(decrypted, message)

        message = "BIGLETTERS"
        shift = 2
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted, shift)
        self.assertEquals(encrypted, "DKINGVVGTU")
        self.assertEquals(decrypted, message)

        message = "smol"
        shift = 6
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted, shift)
        self.assertEquals(encrypted, "ysur")
        self.assertEquals(decrypted, message)

        message = ""
        shift = 1000000000000
        encrypted = encrypt_caesar(message, shift)
        decrypted = decrypt_caesar(encrypted, shift)
        self.assertEquals(encrypted, "")
        self.assertEquals(decrypted, message)

    def test_vigenere(self):
        message = "Biba"
        key = "Boba"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEquals(encrypted, "Cwca")
        self.assertEquals(decrypted, message)

        message = "Raiden"
        key = "Yae"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEquals(encrypted, "Pamber")
        self.assertEquals(decrypted, message)

        message = "AAAAA"
        key = "B"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEquals(encrypted, "BBBBB")
        self.assertEquals(decrypted, message)

        message = "smol"
        key = "letters"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEquals(encrypted, "dqhe")
        self.assertEquals(decrypted, message)

        message = ""
        key = "AmaWannaCheeseBueger"
        encrypted = encrypt_vigenere(message, key)
        decrypted = decrypt_vigenere(encrypted, key)
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

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))