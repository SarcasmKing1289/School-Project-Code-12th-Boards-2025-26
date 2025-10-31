"""ROT13 encryption for text."""
import codecs

def rot13(s):
    return codecs.encode(s, "rot_13")

if __name__ == "__main__":
    s = input("Enter text to encrypt with ROT13: ")
    print(rot13(s))
