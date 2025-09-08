def gcd_euclidean(a, b):
    """Computes the greatest common divisor (GCD) of a and b using an Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(f"GCD of 48 and 18 is: {gcd_euclidean(48, 18)}")