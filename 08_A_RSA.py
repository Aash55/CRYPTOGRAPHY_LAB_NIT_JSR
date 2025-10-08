# Implementation of Standard Asymmetric Block Ciphers-Part I
# a) Rivest-Shamir-Adelman (RSA)
# b) Diffie-Hellman Key Exchange
# c) YAK authenticated key exchange protocol

# Rivest-Shamir-Adelman (RSA)
import math

# --- 1. Simplified Key Generation ---
# Choose two small prime numbers, p and q. (In reality, these are very large)
p = 61
q = 53
n = p * q  # Modulus
phi_n = (p - 1) * (q - 1)  # Euler's totient function

# Choose an integer 'e' (public exponent) such that 1 < e < phi_n and gcd(e, phi_n) = 1
e = 17

# Calculate 'd' (private exponent) such that (d * e) % phi_n = 1
# This is the modular multiplicative inverse of e mod phi_n.
# We'll use a simple loop search for demonstration instead of the Extended Euclidean Algorithm.
d = 0
for k in range(1, phi_n):
    if (k * e) % phi_n == 1:
        d = k
        break

# Public Key: (e, n) = (17, 3233)
# Private Key: (d, n) = (2753, 3233)
print(f"Primes (p, q): ({p}, {q})")
print(f"Modulus n: {n}")
print(f"Phi(n): {phi_n}")
print(f"Public Exponent e: {e}")
print(f"Private Exponent d: {d}")
print("-" * 30)

# --- 2. Encryption and Decryption ---

# Original Message (must be less than n)
# For simplicity, we'll use a number. In a real scenario, text is converted to numbers.
message = 1234
print(f"Original Message (M): {message}")

# --- Encryption (using Public Key: (e, n)) ---
# Ciphertext C = M^e mod n
C = pow(message, e, n)
print(f"Ciphertext (C): {C}")
print("-" * 30)

# --- Decryption (using Private Key: (d, n)) ---
# Decrypted Message M = C^d mod n
M_decrypted = pow(C, d, n)
print(f"Decrypted Message (M'): {M_decrypted}")
print("-" * 30)

# --- Verification ---
if message == M_decrypted:
    print("SUCCESS: The original message matches the decrypted message.")
else:
    print("FAILURE: Decryption error.")