import csv
from dataclasses import dataclass


@dataclass
class Item:

    item_id: int
    name: str
    price: float
    quantity: int

    def total_price(self):
        return self.price * self.quantity

    def to_repr(self) -> dict:
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_repr(data: dict):

        if not isinstance(data["id"], int):
            raise ValueError("item id should be an integer")
        if not isinstance(data["name"], str):
            raise ValueError()

        return Item(
            item_id=data["id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
        )

with open("data.csv", "r") as fin:
    reader = csv.DictReader(fin)
    for line in reader:
        print(Item(
            item_id=int(line["id"]),
            name=line["name"],
            price= float(line["price"]),
            quantity=int(line["quantity"])
        ))
