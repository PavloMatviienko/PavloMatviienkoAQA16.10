import random
from collections import Counter

# Створюємо список з 100 випадкових чисел в межах від 1 до 10
random_numbers = [random.randint(1, 10) for _ in range(100)]
print(f'Список випадкових чисел:{random_numbers}')
# Підраховуємо кількість кожного елементу
counted_numbers = Counter(random_numbers)

# Виводимо результат підрахунку

for number, count in counted_numbers.items():
    print(f'Кількість кожного елементу {number}: {count} разів')