"""Replace the 4th word of a sentence with an underscore and print result."""
def replace_fourth(sentence):
    parts = sentence.split()
    if len(parts) >= 4:
        parts[3] = "_"
    return " ".join(parts)

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(replace_fourth(s))
