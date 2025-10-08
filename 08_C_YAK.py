# Implementation of Standard Asymmetric Block Ciphers-Part I
# a) Rivest-Shamir-Adelman (RSA)
# b) Diffie-Hellman Key Exchange
# c) YAK authenticated key exchange protocol

#YAK authenticated key exchange protocol
import random

def power(a, b, m):
    """Computes (a^b) mod m"""
    return pow(a, b, m)

# 1. System Public Parameters (Shared by everyone)
# Small prime modulus (p) and generator (g) for demonstration
# In a real system, these would be very large cryptographically secure numbers.
p = 23
g = 5
print(f"1. Public Parameters: p={p}, g={g}\n")

# --- ALICE'S SETUP ---
# Alice's static private key (a_priv)
a_priv = random.randint(1, p - 1)
# Alice's static public key (A_pub)
A_pub = power(g, a_priv, p)

# --- BOB'S SETUP ---
# Bob's static private key (b_priv)
b_priv = random.randint(1, p - 1)
# Bob's static public key (B_pub)
B_pub = power(g, b_priv, p)

print(f"2. Static Keys:")
print(f"   Alice's Private Key (a_priv): {a_priv}")
print(f"   Alice's Public Key (A_pub): {A_pub}")
print(f"   Bob's Private Key (b_priv): {b_priv}")
print(f"   Bob's Public Key (B_pub): {B_pub}\n")

# 3. Key Exchange (Ephemeral Key Generation and Exchange)

# --- ALICE'S EPHEMERAL KEYS ---
# Alice's ephemeral private key (x_A)
x_A = random.randint(1, p - 1)
# Alice's ephemeral public key (A_eph) to be sent to Bob
A_eph = power(g, x_A, p)

# --- BOB'S EPHEMERAL KEYS ---
# Bob's ephemeral private key (y_B)
y_B = random.randint(1, p - 1)
# Bob's ephemeral public key (B_eph) to be sent to Alice
B_eph = power(g, y_B, p)

# Exchange step:
# Alice sends A_eph to Bob.
# Bob sends B_eph to Alice.

print(f"3. Ephemeral Exchange:")
print(f"   Alice sends ephemeral public key (A_eph): {A_eph}")
print(f"   Bob sends ephemeral public key (B_eph): {B_eph}\n")


# 4. Shared Secret Computation

# --- ALICE'S COMPUTATION ---
# Alice receives B_pub (static public) and B_eph (ephemeral public) from Bob.
# K = (B_pub * B_eph)^(x_A + a_priv) mod p
base_A = (B_pub * B_eph) % p
exponent_A = x_A + a_priv
K_Alice = power(base_A, exponent_A, p)

# --- BOB'S COMPUTATION ---
# Bob receives A_pub (static public) and A_eph (ephemeral public) from Alice.
# K = (A_pub * A_eph)^(y_B + b_priv) mod p
base_B = (A_pub * A_eph) % p
exponent_B = y_B + b_priv
K_Bob = power(base_B, exponent_B, p)


print("4. Shared Secret Results:")
print(f"   Alice's Shared Secret (K_Alice): {K_Alice}")
print(f"   Bob's Shared Secret (K_Bob):   {K_Bob}")
print("-" * 35)

if K_Alice == K_Bob:
    print("✅ Key Exchange Successful: Secrets Match!")
else:
    print("❌ Key Exchange Failed: Secrets Do Not Match!")

# Verification of the Shared Secret
# The shared secret should be: K = g^((a_priv + x_A) * (b_priv + y_B)) mod p
K_Verify_Exponent = (a_priv + x_A) * (b_priv + y_B)
K_Verify = power(g, K_Verify_Exponent, p)
# print(f"\n[Verification K_Verify: {K_Verify}]") # Optional verification