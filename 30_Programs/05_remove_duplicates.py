"""Delete duplicate values while preserving order."""
def remove_duplicates(seq):
    seen = set()
    out = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

if __name__ == "__main__":
    raw = input("Enter items separated by spaces: ")
    items = raw.split()
    print(remove_duplicates(items))
