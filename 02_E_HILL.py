import numpy as np

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper().replace(" ", "")]

# Function to convert numbers back to text
def numbers_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

# Hill Cipher Encryption
def hill_encrypt(plain_text, key_matrix):
    nums = text_to_numbers(plain_text)
    
    # Padding if odd length
    if len(nums) % 2 != 0:
        nums.append(ord('X') - ord('A'))
    
    cipher_nums = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2])
        result = np.dot(key_matrix, pair) % 26
        cipher_nums.extend(result)
    
    return numbers_to_text(cipher_nums)

# Example usage
key = np.array([[3, 3],
                [2, 5]])   # Example invertible key matrix mod 26

plain = "HELLO"
cipher = hill_encrypt(plain, key)

print("Plain Text :", plain)
print("Cipher Text:", cipher)
