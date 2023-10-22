from datetime import datetime, timedelta

def add_or_subtract_days(input_datetime, days, add=True):
    if add:
        # Додаємо дні за допомогою timedelta
        result_datetime = input_datetime + timedelta(days=days)
    else:
        # Віднімаємо дні за допомогою timedelta
        result_datetime = input_datetime - timedelta(days=days)

    return result_datetime

input_datetime = datetime(year= 2023, month= 10, day= 22, hour= 12, minute= 0, second= 0)
days_to_add_or_subtract = 7
add_days = True  # Якщо True, додаємо дні; якщо False, віднімаємо

result_datetime = add_or_subtract_days(input_datetime, days_to_add_or_subtract, add_days)
print(f'Результат: {result_datetime}')
