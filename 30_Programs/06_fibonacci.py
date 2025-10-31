"""Display n Fibonacci numbers."""
def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

if __name__ == "__main__":
    try:
        n = int(input("How many Fibonacci numbers? ").strip())
        print(fibonacci(n))
    except ValueError:
        print("Please enter an integer.")
