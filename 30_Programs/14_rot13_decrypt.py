"""ROT13 decryption (same as encryption)."""
import codecs

def rot13(s):
    return codecs.encode(s, "rot_13")

if __name__ == "__main__":
    s = input("Enter ROT13 text to decrypt: ")
    print(rot13(s))
