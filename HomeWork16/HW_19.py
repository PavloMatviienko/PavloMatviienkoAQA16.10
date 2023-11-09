import pytest
from train_module import Train, TrainCar

@pytest.fixture
def train_instance():
    train = Train()
    train.add_train_car(TrainCar(1))
    train.add_train_car(TrainCar(2))
    train.add_train_car(TrainCar(3))
    return train

@pytest.mark.smoke
def test_train_car_add_passenger(train_instance):
    train_instance.train_cars[0].add_passenger("Luke Skywalker", "Tatooine", 1)
    assert len(train_instance.train_cars[0]) == 1

@pytest.mark.smoke
def test_train_len(train_instance):
    assert len(train_instance) == 2  # Один локомотив, два вагони

@pytest.mark.regression
def test_train_car_capacity(train_instance):
    train_instance.train_cars[0].add_passenger("Luke Skywalker", "Tatooine", 1)
    train_instance.train_cars[0].add_passenger("Han Solo", "Endor", 2)
    train_instance.train_cars[0].add_passenger("Chubaka", "Kashyyyk", 3)
    assert len(train_instance.train_cars[0]) == 3
    train_instance.train_cars[0].add_passenger("Princess Leia", "Mustafar", 4)  # Пробуємо додати більше пасажирів, ніж є місць
    assert len(train_instance.train_cars[0]) == 3  # Кількість пасажирів не повинна змінитися


