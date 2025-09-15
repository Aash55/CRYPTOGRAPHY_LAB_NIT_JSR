import rsa
import hashlib

# --- RSA Digital Signature ---

# 1. Key Generation
(public_key, private_key) = rsa.newkeys(512)

# Message to be signed
message = "This message is from Alice."

# 2. Signing the message with the private key
# First, create a hash of the message
message_hash = hashlib.sha256(message.encode()).digest()

# Sign the hash with the private key
signature = rsa.sign(message_hash, private_key, 'SHA-256')
print(f"Original Message: {message}")
print(f"Digital Signature: {signature}")
print("--------------------------------------------------")

# 3. Verifying the signature with the public key
try:
    # Hash the received message again
    received_message_hash = hashlib.sha256(message.encode()).digest()

    # Verify the signature against the hash and the public key
    rsa.verify(received_message_hash, signature, public_key)
    print("Verification successful: The signature is valid.")
except rsa.VerificationError:
    print("Verification failed: The signature is invalid.")