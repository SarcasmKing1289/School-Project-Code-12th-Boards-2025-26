"""Count words, characters and vowels in a string (user input)."""
def analyze_text(s):
    words = s.split()
    chars = len(s)
    vowels = sum(1 for ch in s.lower() if ch in "aeiou")
    return {"words": len(words), "characters": chars, "vowels": vowels}

if __name__ == "__main__":
    text = input("Enter text: ")
    print(analyze_text(text))
