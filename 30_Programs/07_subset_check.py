"""Check if all elements of iterable A belong to iterable B."""
def is_subset(a, b):
    return set(a).issubset(set(b))

if __name__ == "__main__":
    a = input("Elements of A (space separated): ").split()
    b = input("Elements of B (space separated): ").split()
    print(is_subset(a, b))
