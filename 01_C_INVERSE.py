def extended_euclidean(a, b):
    """
    Returns gcd(a, b), and coefficients x and y such that: a*x + b*y = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, p):
    """
    Returns the modular inverse of a modulo p using the Extended Euclidean Algorithm.
    Assumes p is a prime number.
    """
    gcd, x, _ = extended_euclidean(a, p)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} modulo {p}")
    else:
        return x % p  # Ensure the result is positive

# Example usage:
a = 17
p = 43
inverse = mod_inverse(a, p)
print(f"The modular inverse of {a} mod {p} is: {inverse}")
