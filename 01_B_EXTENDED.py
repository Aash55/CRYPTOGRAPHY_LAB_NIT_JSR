def extended_gcd(a, b):
    
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)

        x = y1 - (b // a) * x1
        y = x1
        return (gcd,x,y)

# Example usage:
a = 48
b = 18
gcd, x, y = extended_gcd(a, b)

print(f"The GCD of {a} and {b} is {gcd}")
print(f"The Coefficients are x = {x} and y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y} which equals the GCD of {gcd}")