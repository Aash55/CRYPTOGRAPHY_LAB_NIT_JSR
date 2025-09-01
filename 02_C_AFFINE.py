def affine_cipher(text, key_a, key_b, mode='encrypt'):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            if mode == 'encrypt':
                new_char = chr(((key_a * (ord(char) - 65) + key_b) % 26) + 65)
            elif mode == 'decrypt':
                mod_inverse = pow(key_a, -1, 26)
                new_char = chr((mod_inverse * (ord(char) - 65 - key_b + 26)) % 26 + 65)
            result += new_char
        else:
            result += char
    return result

# Example Usage
plaintext = "ATTACK"
key_a = 5  # Must be coprime to 26
key_b = 8
encrypted_text = affine_cipher(plaintext, key_a, key_b, 'encrypt')
decrypted_text = affine_cipher(encrypted_text, key_a, key_b, 'decrypt')

print(f"\nAffine Cipher:")
print(f"Plaintext: {plaintext}")
print(f"Keys (a, b): ({key_a}, {key_b})")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")