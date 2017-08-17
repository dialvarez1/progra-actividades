from random import randint
from abc import ABCMeta, abstractmethod


class Product(metaclass = ABCMeta):

	SKU = 0

	def __init__(self, name, price):
		self._name = name
		self._price = price
		self.SKU = Product.SKU
		Product.SKU += 1

	def __str__(self):
		return "[" + str(self.SKU) + "] " + self.name + " $" + str(self.price)


class Food(Product, metaclass = ABCMeta):

        
	def __init__(self, name, price, expire_date, calories, proteins, carbs, fats):
		super().__init__(name, price)
		self._expire_date = expire_date
		self._calories = calories
		self._proteins = proteins
		self._carbs = carbs
		self._fats = fats

	def nutrition_data(self, grams = 100):
		print("Calorías = " + str(self._calories*100/grams) + " (kcal)\nProteínas = " + str(self._proteins*100/grams) + " (g)\nCarbohidratos = " + str(self._carbs*100/grams) + " (g)\nGrasa = " + str(self._fats*100/grams) + " (g)")


class Lacteal(Food):

	def __init__ (self, name, price, expire_date, calories, proteins, carbs, fats, calcium):
		super().__init__(name, price, expire_date, calories, proteins, carbs, fats)
		self._calcium = calcium

	def nutrition_data(self, grams = 100):
		print("Calorías = " + str(self._calories*100/grams) + " (kcal)\nProteínas = " + str(self._proteins*100/grams) + " (g)\nCarbohidratos = " + str(self._carbs*100/grams) + " (g)\nGrasa = " + str(self._fats*100/grams) + " (g)\nCalcio = " + str(self._calcium*100/grams) + "(mg)")




class Clothes(Product):

	def __init__(self, size):
		self._size = size



