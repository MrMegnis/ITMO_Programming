def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    symbols_amount = ord('z') - ord('a') + 1
    text_index = 0
    key_index = 0
    keyword = keyword.upper()
    while text_index < len(plaintext):
        current_shift = ord(keyword[key_index]) - ord("A")
        current_symbol = plaintext[text_index]
        if current_symbol.isalpha():
            if current_symbol.isupper():
                ciphertext += chr(ord("A") + (ord(current_symbol) - ord("A") + current_shift) % symbols_amount)
            else:
                ciphertext += chr(ord("a") + (ord(current_symbol) - ord("a") + current_shift) % symbols_amount)
        else:
            ciphertext += current_symbol
        text_index += 1
        key_index = (key_index + 1) % len(keyword)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    symbols_amount = ord('z') - ord('a') + 1
    new_key = "".join([chr(2 * ord("A") + symbols_amount - ord(i)) for i in keyword.upper()])
    plaintext = encrypt_vigenere(ciphertext, new_key)
    # PUT YOUR CODE HERE
    return plaintext

if __name__ == "__main__":
    print(decrypt_vigenere("PYTHON", "A"))