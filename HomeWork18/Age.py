
import datetime

birth_day = datetime.date(year=1992, month=4, day=4)
today = datetime.date(year=2023, month=10, day=22)
print(f'Точний вік в роках:{int((today-birth_day).days / (365.2425))}рік')


from datetime import datetime

def calculate_age(birthdate):

    current_datetime = datetime.now()

    age = current_datetime - birthdate

    current_timestamp = current_datetime.timestamp()

    return age, current_timestamp

birthdate = datetime(year = 1992, month= 4, day= 1)

age, timestamp = calculate_age(birthdate)
print("Ваш вік:", age)
print("Timestamp поточного часу:", timestamp)