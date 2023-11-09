class TrainCar:
    def __init__(self, number, capacity=10):
        self.number = number
        self.passengers = []
        self.capacity = capacity

    def add_passenger(self, passenger_name, destination, place):
        if len(self.passengers) < self.capacity:
            passenger_info = {
                "passenger_name": passenger_name,
                "destination": destination,
                "place": place
            }
            self.passengers.append(passenger_info)
        else:
            print(f"Вагон {self.number}: Неможливо додати пасажира, всі місця зайняті.")

    def __str__(self):
        result = f'"traincart": "{self.number}"\n'
        for passenger in self.passengers:
            result += f'\n"passenger_name": "{passenger["passenger_name"]}",\n"destination": "{passenger["destination"]}",\n"place": {passenger["place"]}\n'
        return result

    def __len__(self):
        return len(self.passengers)


class Train:
    def __init__(self):
        self.train_cars = []

    def add_train_car(self, train_car):
        self.train_cars.append(train_car)

    def __str__(self):
        result = ""
        for train_car in self.train_cars:
            result += str(train_car)
        return result

    def __len__(self):
        return len(self.train_cars) - 1  # віднімаємо локомотив


# Створення потягу
train = Train()

# Додавання вагонів до потягу
train.add_train_car(TrainCar(1))
train.add_train_car(TrainCar(2))
train.add_train_car(TrainCar(3))

# Додавання пасажирів до вагонів
train.train_cars[0].add_passenger("Luke Skywalker", "Tatooine", 1)
train.train_cars[0].add_passenger("Han Solo", "Endor", 2)

train.train_cars[1].add_passenger("Chubaka", "Kashyyyk", 3)
train.train_cars[1].add_passenger("Princess Leia", "Mustafar", 4)

# Вивід інформації про потяг та вагони в консоль
print("Потяг:")
print(train)
print(f"\nКількість вагонів без локомотива: {len(train)}")
