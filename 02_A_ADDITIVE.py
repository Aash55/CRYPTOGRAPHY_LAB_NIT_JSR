def additive_cipher(text, key, mode='encrypt'):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            if mode == 'encrypt':
                new_char = chr(((ord(char) - 65 + key) % 26) + 65)
            elif mode == 'decrypt':
                new_char = chr(((ord(char) - 65 - key) % 26) + 65)
            result += new_char
        else:
            result += char
    return result

# Example Usage
plaintext = "HELLO WORLD"
key = 3
encrypted_text = additive_cipher(plaintext, key, 'encrypt')
decrypted_text = additive_cipher(encrypted_text, key, 'decrypt')

print(f"Additive Cipher:")
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
