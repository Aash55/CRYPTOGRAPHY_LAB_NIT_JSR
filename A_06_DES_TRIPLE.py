# Implementation of Standard Symmetric Block Ciphers 
# a) Data Encryption Standard (DES)
# b) Triple DES
# c) Advance Encryption Standard (AES)

# Triple DES with 2 Keys
import A_05_DES as DES

def tripleDESEncryption(plaintext, key1, key2):
    return DES.desEncryption(DES.desDecryption(DES.desEncryption(plaintext, key1), key2), key1)

def tripleDESDecryption(ciphertext, key1, key2):
    return DES.desDecryption(DES.desEncryption(DES.desDecryption(ciphertext, key1), key2), key1)

if __name__ == "__main__":
    plaintext = "ABCD132536654321"
    plaintext = DES.hexToBin(plaintext)

    key1 = "4133957999BDCCF9"
    key1 = DES.hexToBin(key1)

    key2 = "4133957999BDCCF2"
    key2 = DES.hexToBin(key2)

    print("Plaintext:", DES.binToHex(plaintext), "Key1:", DES.binToHex(key1), "Key2:", DES.binToHex(key2))
    print()

    ciphertext = tripleDESEncryption(plaintext, key1, key2)

    print("Encryption:")
    print("Ciphertext:", DES.binToHex(ciphertext))
    print()
    print("Decryption: ")
    print("Plaintext:", DES.binToHex(tripleDESDecryption(ciphertext, key1, key2)), "\n")