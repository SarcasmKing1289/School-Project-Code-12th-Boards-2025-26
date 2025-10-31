"""Insertion sort implementation."""
def insertion_sort(seq):
    a = list(seq)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__ == "__main__":
    raw = input("Enter numbers separated by spaces: ")
    try:
        nums = [float(x) for x in raw.split()]
        print(insertion_sort(nums))
    except ValueError:
        print("Invalid input.")
