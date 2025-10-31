"""Count the number of occurrences of a given word in a text file."""
from pathlib import Path

def count_word_in_file(path, word):
    p = Path(path)
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(path)
    text = p.read_text(encoding="utf-8", errors="ignore").lower()
    return text.split().count(word.lower())

if __name__ == "__main__":
    path = input("File path: ").strip()
    word = input("Word to count: ").strip()
    try:
        print(count_word_in_file(path, word))
    except Exception as e:
        print("Error:", e)
