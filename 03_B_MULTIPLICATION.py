# Function for regular polynomial multiplication
def poly_mult_normal(poly1, poly2, irreducible_poly):
    """
    Multiplies two polynomials and reduces the result modulo an irreducible polynomial.
    """
    # Standard multiplication
    len1, len2 = len(poly1), len(poly2)
    temp_result = [0] * (len1 + len2 - 1)
    
    for i in range(len1):
        if poly1[i] == 1:
            for j in range(len2):
                if poly2[j] == 1:
                    # XOR at the corresponding position
                    temp_result[i + j] ^= 1

    # Modulo reduction (long division)
    irred_degree = len(irreducible_poly) - 1
    
    while len(temp_result) >= irred_degree + 1:
        if temp_result[0] == 1:
            # Shift irreducible polynomial to align with the highest bit
            shift_amount = len(temp_result) - len(irreducible_poly)
            shifted_irred = [0] * shift_amount + irreducible_poly
            
            # XOR the temporary result with the shifted irreducible poly
            for i in range(len(temp_result)):
                temp_result[i] ^= shifted_irred[i]

        # Remove leading zeros
        while len(temp_result) > 1 and temp_result[0] == 0:
            temp_result.pop(0)

    return temp_result

# Example Usage
p1 = [1, 1] # x + 1
p2 = [1, 0, 1] # x^2 + 1
# Irreducible polynomial for GF(2^3) (e.g., x^3 + x + 1)
irred = [1, 0, 1, 1] 
mult_result = poly_mult_normal(p1, p2, irred)
print(f"\nPolynomial 1 (binary): {p1}")
print(f"Polynomial 2 (binary): {p2}")
print(f"Irreducible Polynomial: {irred}")
print(f"Multiplication Result (normal approach): {mult_result}")