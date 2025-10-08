# Implementation of Standard Asymmetric Block Ciphers-Part I
# a) Rivest-Shamir-Adelman (RSA)
# b) Diffie-Hellman Key Exchange
# c) YAK authenticated key exchange protocol

# Diffie-Hellman Key Exchange
import random

def diffie_hellman(p_val, g_val):
    """
    Simulates the Diffie-Hellman Key Exchange protocol.
    
    Args:
        p_val (int): The shared prime modulus (p).
        g_val (int): The shared primitive root modulo p (g).
    
    Returns:
        tuple: A tuple containing (shared_key_A, shared_key_B)
    """

    print("--- 1. Publicly Shared Values ---")
    print(f"Prime Modulus (p): {p_val}")
    print(f"Generator (g): {g_val}\n")

    # --- Step 1: Private Key Selection ---
    # Alice and Bob secretly choose their private keys (integers).
    # We use a fixed range for this example, but it's typically much larger.
    
    # Alice's private key (a)
    private_key_A = random.randint(2, p_val - 2) 
    # Bob's private key (b)
    private_key_B = random.randint(2, p_val - 2)
    
    print("--- 2. Private Key Selection (Secret) ---")
    print(f"Alice's Private Key (a): {private_key_A}")
    print(f"Bob's Private Key (b): {private_key_B}\n")

    # --- Step 2: Public Key Calculation ---
    # Alice calculates her public key: A = (g^a) mod p
    # Bob calculates his public key: B = (g^b) mod p
    
    # Python's built-in `pow(base, exp, mod)` is efficient for this.
    public_key_A = pow(g_val, private_key_A, p_val)
    public_key_B = pow(g_val, private_key_B, p_val)

    print("--- 3. Public Key Exchange (Sent over insecure channel) ---")
    print(f"Alice's Public Key (A): {public_key_A}")
    print(f"Bob's Public Key (B): {public_key_B}\n")
    
    # --- Step 3: Shared Secret Key Calculation ---
    # Alice computes the shared key: s_A = (B^a) mod p
    # Bob computes the shared key: s_B = (A^b) mod p
    
    shared_key_A = pow(public_key_B, private_key_A, p_val) # Alice uses Bob's public key (B)
    shared_key_B = pow(public_key_A, private_key_B, p_val) # Bob uses Alice's public key (A)

    print("--- 4. Shared Secret Key Calculation (Secret) ---")
    print(f"Alice's Calculated Shared Key: {shared_key_A}")
    print(f"Bob's Calculated Shared Key: {shared_key_B}\n")

    return shared_key_A, shared_key_B

# --- Main Execution ---
# Standard Diffie-Hellman uses large, cryptographically secure primes.
# These values are small for demonstration purposes.

# Shared Prime Modulus (p) - must be a large prime
P = 23
# Shared Generator (g) - must be a primitive root modulo P
G = 5

final_key_A, final_key_B = diffie_hellman(P, G)

# --- Verification ---
print("--- 5. Verification ---")
if final_key_A == final_key_B:
    print(f"✅ Success! Both parties have established the same shared secret key: {final_key_A}")
else:
    print("❌ Error! Keys do not match.")