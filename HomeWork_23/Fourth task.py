strings = ["apple", "banana", "kiwi", "grape", "watermelon", "orange"]

max_min_lengths = lambda strings: (
    max(strings, key=len),
    min(strings, key=len)
)

max_str, min_str = max_min_lengths(strings)
print(f"Слово з максимальною довжиною: {max_str}")
print(f"Слово з мінімальною довжиною: {min_str}")