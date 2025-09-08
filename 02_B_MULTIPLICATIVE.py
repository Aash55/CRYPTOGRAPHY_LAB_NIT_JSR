def gcd_euclidean(a, b):
    """Computes the greatest common divisor (GCD) of a and b using an Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_cipher(text, key, mode='encrypt'):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            if mode == 'encrypt':
                new_char = chr(((ord(char) - 65) * key) % 26 + 65)
            elif mode == 'decrypt':
                mod_inverse = pow(key, -1, 26)
                new_char = chr(((ord(char) - 65) * mod_inverse) % 26 + 65)
            result += new_char
        else:
            result += char
    return result

# Example Usage
plaintext = "CRYPTO"
key = 9

encrypted_text = multiplicative_cipher(plaintext, key, 'encrypt')
decrypted_text = multiplicative_cipher(encrypted_text, key, 'decrypt')

print(f"\nMultiplicative Cipher:")
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")