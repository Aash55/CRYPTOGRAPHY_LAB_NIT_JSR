def playfair_cipher(text, key):
    key = key.upper().replace('J', 'I')
    text = text.upper().replace('J', 'I')
    
    # 1. Create key matrix
    key_matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    seen = set()
    for char in key + alphabet:
        if char not in seen:
            key_matrix.append(char)
            seen.add(char)
    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]

    # 2. Prepare plaintext
    prepared_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i+1]:
            prepared_text += text[i] + 'X'
            i += 1
        elif i + 1 < len(text):
            prepared_text += text[i:i+2]
            i += 2
        else:
            prepared_text += text[i] + 'X'
            i += 1
    
    # 3. Encrypt
    def find_pos(char):
        for r, row in enumerate(key_matrix):
            if char in row:
                return r, row.index(char)
    
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        c1, c2 = prepared_text[i], prepared_text[i+1]
        r1, c1_pos = find_pos(c1)
        r2, c2_pos = find_pos(c2)
        
        if r1 == r2:  # Same row
            ciphertext += key_matrix[r1][(c1_pos + 1) % 5] + key_matrix[r2][(c2_pos + 1) % 5]
        elif c1_pos == c2_pos:  # Same column
            ciphertext += key_matrix[(r1 + 1) % 5][c1_pos] + key_matrix[(r2 + 1) % 5][c2_pos]
        else:  # Rectangle
            ciphertext += key_matrix[r1][c2_pos] + key_matrix[r2][c1_pos]
            
    return ciphertext

# Example Usage (Encryption Only)
plaintext = "INSTRUMENTS"
key = "MONARCHY"
encrypted_text = playfair_cipher(plaintext, key)

print(f"\nPlayfair Cipher (Encryption):")
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")