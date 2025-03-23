# class Animal:
#     def printSize(self):
#         print("very")

# class Hamster(Animal):
#     def printSize(self):
#         super().printSize()
#         print("small")

# obj = Hamster()
# obj.printSize()


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def makesound(self):
#         print("yes")

# class MarineAnimal(Animal):
#     def makesound(self):
#         print("No Sound")

# class Fish(MarineAnimal):
#     pass

# obj = Fish()
# obj.makesound()

# class User:
#     def __init__(self):
#         User.count += 1

# User.count = 0

# obj1 = User()
# obj2 = User()
# obj3 = User()
# print(User.count)

# from typing import Any


# class Myclass:
#     def __init__(self, x) -> None:
#         self.x = x
#     def __call__(self, y) -> Any:
#         return self.x * y
    
# obj = Myclass(2)
# print(obj(3))

# class Doubler(int):
#     def __mul__(self, other):
#         return super().__mul__(other + 3)
    
# obj = Doubler(3)
# result = obj * 5
# print(result)

# class Product:
#     pass

# prods = []

# for i in range(1,4):
#     obj = Product()
#     obj.prize = i * 6
#     prods.append(obj)

# for prod in prods:
#     if prod.prize > 10:
#         print(prod.prize)

# data = [1,2,3,4,5]
# a, *_, b = data
# print(a, b)

# from typing import Union, TypeVar, Iterable

# def square_root(num: Union[int, float]):
#     return num ** 0.5
    
# print(square_root(2))

# T = TypeVar("V")
# def first_ele(items: Iterable[T]):
#     return next(iter(items))
# print(first_ele("venky"))
# print(first_ele("venky"))

# class Apple:
#     def __init__(self) -> None:
#         print("1")
# class Fruit(Apple):
#     def __init__(self) -> None:
#         print("2")

# obj = Fruit()

# lst = ["p", 20, "s", 4.5]
# items = iter(lst)
# print(next(items))
# print(next(items))

# from abc import ABC, abstractmethod
# class Shop (ABC):
#     @abstractmethod
#     def calcRevenue (self):
#         pass
# class ClothesShop (Shop):
#     def calcRevenue (self):
#         return self.sellsCount * 5
# obj = ClothesShop()
# obj.sellsCount = 20
# print(obj.calcRevenue())

# password generator.
import random
import string
total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)
