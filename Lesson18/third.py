from abc import ABC, abstractmethod

class Dish(ABC):
    @abstractmethod
    def get_dish(self):
        pass

class Risotto(Dish):
    def get_dish(self):
        return "Risotto"

class Pasta(Dish):
    def get_dish(self):
        return "Pasta"

class Pizza(Dish):
    def get_dish(self):
        return "Pizza"

class OrderPart:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def get_order(self):
        return [dish.get_dish() for dish in self.dishes]

# Приклад використання
order_part = OrderPart()
order_part.add_dish(Risotto())
order_part.add_dish(Pasta())
order_part.add_dish(Pizza())

print(order_part.get_order())