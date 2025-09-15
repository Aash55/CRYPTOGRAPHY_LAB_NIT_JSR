import rsa

# --- RSA Encryption and Decryption ---

# 1. Key Generation (in a real scenario, key size should be much larger)
(public_key, private_key) = rsa.newkeys(512)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print("--------------------------------------------------")

# 2. Encryption
message = "Hello, this is a secret message."
encrypted_message = rsa.encrypt(message.encode(), public_key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print("--------------------------------------------------")

# 3. Decryption
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print(f"Decrypted Message: {decrypted_message}")