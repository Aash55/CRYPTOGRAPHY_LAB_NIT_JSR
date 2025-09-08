# Function for computationally efficient multiplication
def poly_mult_efficient(poly1, poly2, irreducible_poly):
    """
    Multiplies two polynomials using a shift-and-XOR method.
    """
    res = [0] * (len(irreducible_poly) - 1)
    
    # Iterate through each term of the first polynomial from left to right
    for p1_term in poly1:
        # Perform the shift
        res.append(0)
        
        # If the highest bit of the result is 1, XOR with the irreducible polynomial
        if res[0] == 1:
            # XOR the result with the irreducible polynomial
            for i in range(len(irreducible_poly)):
                res[i] ^= irreducible_poly[i]

        # If the current term of the first polynomial is 1, XOR with the second polynomial
        if p1_term == 1:
            # We need to make sure poly2 is the correct length for XORing
            padded_poly2 = [0] * (len(res) - len(poly2)) + poly2
            for i in range(len(res)):
                res[i] ^= padded_poly2[i]
                
    # Remove leading zeros
    while len(res) > 1 and res[0] == 0:
        res.pop(0)

    return res

# Example Usage
p1_ef = [1, 1] # x + 1
p2_ef = [1, 0, 1] # x^2 + 1
irred_ef = [1, 0, 1, 1] # Irreducible polynomial for GF(2^3)
mult_result_efficient = poly_mult_efficient(p1_ef, p2_ef, irred_ef)

print(f"\nPolynomial 1 (binary): {p1_ef}")
print(f"Polynomial 2 (binary): {p2_ef}")
print(f"Irreducible Polynomial: {irred_ef}")
print(f"Multiplication Result (efficient approach): {mult_result_efficient}")