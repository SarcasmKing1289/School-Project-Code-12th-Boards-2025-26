"""Find median of user-provided numbers using statistics module."""
import statistics

def median_of_numbers(nums):
    return statistics.median(nums)

if __name__ == "__main__":
    raw = input("Enter numbers separated by spaces: ")
    try:
        nums = [float(x) for x in raw.split()]
        print("Median:", median_of_numbers(nums))
    except ValueError:
        print("Invalid input; please enter numeric values.")
