# cleanup_fixed.py (fixed via list comprehension)

def remove_short(names, min_len):
    return [n for n in names if len(n) >= min_len]

# self-test (now correct)
if __name__ == "__main__":
    data = ["A", "B", "Cat", "Do"]
    print(remove_short(data, 2))
    # Output: ['Cat', 'Do']