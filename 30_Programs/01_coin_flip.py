"""Coin flipping simulator."""
import random

def flip_coin(n):
    results = {"heads": 0, "tails": 0}
    for _ in range(n):
        results["heads" if random.choice([True, False]) else "tails"] += 1
    return results

if __name__ == "__main__":
    try:
        n = int(input("Number of flips: ").strip())
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer.")
    else:
        print(flip_coin(n))
