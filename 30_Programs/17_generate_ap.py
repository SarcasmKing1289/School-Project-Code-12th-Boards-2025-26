"""Generate an arithmetic progression given start, end and number of terms (including endpoints)."""
def generate_ap(a, b, n):
    if n == 1:
        return [a]
    step = (b - a) / (n - 1)
    return [a + i * step for i in range(n)]

if __name__ == "__main__":
    try:
        a = float(input("Start value: ").strip())
        b = float(input("End value: ").strip())
        n = int(input("Number of terms: ").strip())
        if n <= 0:
            raise ValueError
        print(generate_ap(a, b, n))
    except ValueError:
        print("Invalid input.")
