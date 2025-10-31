"""Convert numbers into words (supports 0..9999)."""
ONES = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}
TENS = {
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
}

def number_to_words(n):
    if not (0 <= n <= 9999):
        raise ValueError("Supported range: 0..9999")
    if n < 20:
        return ONES[n]
    if n < 100:
        tens, rem = divmod(n, 10)
        return TENS[tens] + ("" if rem == 0 else "-" + ONES[rem])
    if n < 1000:
        hundreds, rem = divmod(n, 100)
        return ONES[hundreds] + " hundred" + ("" if rem == 0 else " " + number_to_words(rem))
    thousands, rem = divmod(n, 1000)
    return number_to_words(thousands) + " thousand" + ("" if rem == 0 else " " + number_to_words(rem))

if __name__ == "__main__":
    try:
        n = int(input("Enter integer (0-9999): ").strip())
        print(number_to_words(n))
    except Exception as e:
        print("Error:", e)
