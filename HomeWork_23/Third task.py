is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 else False

input_string = input("Введіть рядок: ")
result = "Число" if is_number(input_string) else "Не число"
print(result)