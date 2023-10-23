def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    symbols_amount = ord('z') - ord('a') + 1
    actual_shift = shift % symbols_amount
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                ciphertext += chr(ord("A") + (ord(i) - ord("A") + actual_shift) % symbols_amount)
            else:
                ciphertext += chr(ord("a") + (ord(i) - ord("a") + actual_shift) % symbols_amount)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    symbols_amount = ord('z') - ord('a') + 1
    actual_shift = shift % symbols_amount
    plaintext = encrypt_caesar(ciphertext, symbols_amount - actual_shift)
    return plaintext