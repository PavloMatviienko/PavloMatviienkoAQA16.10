from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class A(Base):
    def method1(self):
        print("Method 1 in class A")

    def method2(self):
        print("Method 2 in class A")


class B(Base):
    def method1(self):
        print("Method 1 in class B")

    def method2(self):
        print("Method 2 in class B")


class C(Base):
    def method1(self):
        print("Method 1 in class C")

    def method2(self):
        print("Method 2 in class C")


def main():
    # Приклад
    obj_a = A()
    obj_b = B()
    obj_c = C()

    obj_a.method1()
    obj_a.method2()

    obj_b.method1()
    obj_b.method2()

    obj_c.method1()
    obj_c.method2()


if __name__ == "__main__":
    main()
