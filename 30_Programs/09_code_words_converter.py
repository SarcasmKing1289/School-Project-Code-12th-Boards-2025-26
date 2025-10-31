"""Convert code-words to full words using a small mapping."""
MAPPING = {
    "brb": "be right back",
    "idk": "I don't know",
    "omw": "on my way",
    "ttyl": "talk to you later",
}

def convert(text):
    parts = text.split()
    return " ".join(MAPPING.get(p.lower(), p) for p in parts)

if __name__ == "__main__":
    s = input("Enter text with code-words: ")
    print(convert(s))
