from datetime import datetime
from typing import List


class InventoryItem:
    def __init__(self, name: str, quantity: int, added_on: datetime):
        self.name = name
        self.quantity = quantity
        self.added_on = added_on


class InventorySystem:
    def __init__(self):
        self.inventory_items: List[InventoryItem] = []
        self.start_program = True
