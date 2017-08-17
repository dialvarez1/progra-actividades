from random import randint
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    SKU = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.SKU = Product.SKU
        Product.SKU += 1

    def __str__(self):
        return "[" + str(self.SKU) + "] " + self.name + " $" + str(self.price)


class Food(Product, metaclass=ABCMeta):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats):
        super().__init__(name, price)
        self._expire_date = expire_date
        self._calories = calories
        self._proteins = proteins
        self._carbs = carbs
        self._fats = fats

    def nutrition_data(self, grams=100):
        print("Calorías = " + str(
            self._calories * grams / 100) + " (kcal)\nProteínas = " + str(
            self._proteins * grams / 100) + " (g)\nCarbohidratos = " + str(
            self._carbs * grams / 100) + " (g)\nGrasa = " + str(
            self._fats * grams / 100) + " (g)")


class Lacteal(Food, metaclass=ABCMeta):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, calcium):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats)
        self._calcium = calcium

    def nutrition_data(self, grams=100):
        print("Calorías = " + str(
            self._calories * grams / 100) + " (kcal)\nProteínas = " + str(
            self._proteins * grams / 100) + " (g)\nCarbohidratos = " + str(
            self._carbs * grams / 100) + " (g)\nGrasa = " + str(
            self._fats * grams / 100) + " (g)\nCalcio = " + str(
            self._calcium * grams / 100) + "(mg)")


class Verdure(Food, metaclass=ABCMeta):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, vitC):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats)
        self.vitC = vitC

    def nutrition_data(self, grams=100):
        print("Calorías = " + str(
            self._calories * grams / 100) + " (kcal)\nProteínas = " + str(
            self._proteins * grams / 100) + " (g)\nCarbohidratos = " + str(
            self._carbs * grams / 100) + " (g)\nGrasa = " + str(
            self._fats * grams / 100) + " (g)\nVitamina C = " + str(
            self.vitC * grams / 100) + "(mg)")


class Meat(Food, metaclass=ABCMeta):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, animal):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats)
        self.animal = animal

    def nutrition_data(self, grams=100):
        print("Calorías = " + str(
            self._calories * grams / 100) + " (kcal)\nProteínas = " + str(
            self._proteins * grams / 100) + " (g)\nCarbohidratos = " + str(
            self._carbs * grams / 100) + " (g)\nGrasa = " + str(
            self._fats * grams / 100) + " (g)\nAnimal: " + self.animal)


class Lomo(Meat):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, animal="vacuno"):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats, animal)


class Manzana(Verdure):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, vitC):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats, vitC)


class Leche(Lacteal):
    def __init__(self, name, price, expire_date, calories, proteins, carbs,
                 fats, calcium):
        super().__init__(name, price, expire_date, calories, proteins, carbs,
                         fats, calcium)


class Clothes(Product, metaclass=ABCMeta):
    def __init__(self, name, price, size, sex):
        super().__init__(name, price)
        self.size = size
        self.sex = sex

    def size_data(self):
        print("Talla = " + str(self.size) + "\nGenero = " + str(self.sex))


class PantalonAzul(Clothes):
    def __init__(self, name, price, size, sex):
        super().__init__(name, price, size, sex)
