"""Check if the input string is a palindrome (ignoring spaces and case)."""
def is_palindrome(s):
    filtered = "".join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

if __name__ == "__main__":
    s = input("Enter text: ")
    print(is_palindrome(s))
