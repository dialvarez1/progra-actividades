import collections as col
import datetime as dt
import enum
import random as rnd

from Actividad import *


class Human:

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def say(self, message):
        print(f"{self.name}: {message}")

    def greet(self, other=None):
        name = f", {other.name}" if other is not None else ""
        self.say(f"Buenos días{name}")


class Client(Human):

    class Preference(enum.Enum):
        vegan = enum.auto()
        vegetarian = enum.auto()
        omnivore = enum.auto()

    @classmethod
    def create_random(cls):
        names = ["Pedro", "María", "Paz", "Juan"]
        return cls(rnd.choice(names), dt.date(rnd.randint(1950, 2000),
                                              rnd.randint(1, 12),
                                              rnd.randint(1, 28)),
                   rnd.randint(20000, 100000), rnd.choice(list(cls.Preference)),
                   bool(rnd.getrandbits(1)))

    def __init__(self, name, birth, cash, alimentary_preference, frequent):
        super().__init__(name, birth)
        self._cart = col.defaultdict(int)
        self._cash = cash
        self._alimentary_preference = alimentary_preference
        today = dt.date.today()
        self.third_age = birth < today.replace(year=today.year-18)
        self.frequent = frequent

    def can_buy(self, product):
        if self._alimentary_preference == Client.Preference.omnivore:
            return True
        if self._alimentary_preference == Client.Preference.vegetarian:
            return not isinstance(product, Meat)
        if self._alimentary_preference == Client.Preference.omnivore:
            return not isinstance(product, (Meat, Lacteal))

    def add_product(self, product, quantity):
        self._cart[product] += quantity

    def checkout(self):
        cart = self._cart
        self._cart = col.defaultdict(int)
        return cart

    def pay(self, amount):
        if amount <= self._cash:
            self._cash -= amount
            return True
        else:
            return False


class Cashier(Human):

    @staticmethod
    def _apply_discount(client, product, quantity):
        discounts = set()
        discounts.add(0)
        if client.frequent:
            if isinstance(product, Clothes):
                discounts.add(10)
            elif isinstance(product, Food):
                discounts.add(15)
        if client.third_age:
            discounts.add(10)
        return quantity * product.price * (100 - max(discounts)) / 100

    def calculate_price(self, client, cart):
        total = 0
        for product, quantity in cart.items():
            price = self._apply_discount(client, product, quantity)
            self.say(f"{product.name}, {quantity} "
                     f"unidad{'es' if quantity > 1 else ''}, ${price}")
            total += price
        self.say(f"En total son ${total}")
        return total


class Simulation:

    def __init__(self, clients, cashiers, products):
        self.clients = clients
        self.cashiers = cashiers
        self.products = products

    def run(self):
        while self.clients:
            for client in self.clients:
                if self.products and rnd.getrandbits(2):
                    product, stock = rnd.choice(tuple(self.products.items()))
                    if not stock:
                        continue
                    if client.can_buy(product):
                        quantity = rnd.randint(1, stock)
                        self.products[product] -= quantity
                        client.add_product(product, quantity)
                        print(f"{client.name} ha añadido {quantity} "
                              f"{product.name} a su carro")
                    else:
                        print(f"{client.name} ha considerado comprar "
                              f"{product.name}, pero ha decidido no hacerlo")
                else:
                    cashier = rnd.choice(self.cashiers)
                    cart = client.checkout()
                    if cart:
                        cashier.greet(client if client.frequent else None)
                        if rnd.getrandbits(2):
                            client.greet(cashier)
                        price = cashier.calculate_price(client, cart)
                        if not client.pay(price):
                            print("f{client.name} no ha podido pagar")
                            self.products.extend(cart)
                        else:
                            print(f"{client.name} paga")
                    self.clients.remove(client)
                    print(f"{client.name} se retira")


class Prod(Product):
    pass


def main():
    clients = [Client.create_random() for _ in range(10)]
    clients.append(Client("Viejo", dt.date(1950, 5, 31), 50000,
                          Client.Preference.omnivore, True))
    cashiers = [Cashier("Cajero", dt.date(1970, 3, 3))]
    products = {Prod("Papas", 100): 20,
                Prod("Polera", 30): 10}
    Simulation(clients, cashiers, products).run()


if __name__ == '__main__':
    main()
