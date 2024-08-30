from typing import Dict, List


class Warehouse:
    def __init__(self, capacity: int, list_of_products: list[str]):
        self.capacity = capacity
        self.list_of_products = list_of_products
        self.map_of_products: Dict[str, int] = {}
        for string in list_of_products:
            self.map_of_products[string] = 0
        self.map_of_products = self.map_of_products

    def has(self, item: str) -> bool:
        if item in self.map_of_products.keys() and self.map_of_products[item] == 0:
            return False
        return item in self.map_of_products.keys()

    def has_util(self, item: str) -> bool:
        return item in self.map_of_products.keys()

    def get(self, item: str) -> int:
        if self.has_util(item):
            return self.map_of_products[item]
        else:
            return 0

    def list(self) -> List[str]:
        return self.list_of_products

    def add(self, amount: int, item: str):
        if self.has_util(item) and (self.map_of_products[item] + amount) <= self.capacity:
            self.map_of_products[item] += amount

    def remove(self, amount, item):
        if self.has_util(item):
            if self.map_of_products[item] >= amount:
                self.map_of_products[item] -= amount
