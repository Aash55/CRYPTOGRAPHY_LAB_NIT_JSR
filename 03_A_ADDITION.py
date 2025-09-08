# Function to add two polynomials
def poly_add(poly1, poly2):
    """
    Adds two polynomials represented as lists of coefficients.
    Example: poly1 = [1, 0, 1] (x^2 + 1), poly2 = [1, 1] (x + 1)
    Result: [1, 1, 0] (x^2 + x)
    """
    # Pad the shorter polynomial with zeros to match the length
    max_len = max(len(poly1), len(poly2))
    poly1 = [0] * (max_len - len(poly1)) + poly1
    poly2 = [0] * (max_len - len(poly2)) + poly2
    
    result = [0] * max_len
    for i in range(max_len):
        result[i] = poly1[i] ^ poly2[i] # XOR operation for addition
    
    # Remove leading zeros
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

# Example Usage
p1 = [1, 0, 1, 1] # x^3 + x + 1
p2 = [1, 1, 0, 0] # x^3 + x^2
sum_poly = poly_add(p1, p2)
print(f"Polynomial 1 (binary): {p1}")
print(f"Polynomial 2 (binary): {p2}")
print(f"Addition Result (binary): {sum_poly}")