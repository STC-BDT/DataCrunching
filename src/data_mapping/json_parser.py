import json
from dataclasses import dataclass


# class Item:
#
#     def __init__(self, item_id: int, name: str, price: float, quantity: int):
#         self.quantity = quantity
#         self.price = price
#         self.item_id = item_id
#         self.name = name
#
#         if not isinstance(self.item_id, int):
#             raise ValueError("item id should be an integer")
#
#     def __eq__(self, other):
#         return self.item_id == other.item_id and
#
#     def total_price(self) -> float:
#         return self.price * self.quantity


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


with open("data.json", "r") as fin:
    data = json.load(fin)

    my_item = Item.from_repr(data)
    print(my_item)

raw_item = my_item.to_repr()

print(raw_item)

with open("data2.json", "w") as fout:
    json.dump(raw_item, fout)


# def parse_item(data: dict) -> Item:
#     if not isinstance(data["id"], int):
#         raise ValueError("item id should be an integer")
#     if not isinstance(data["name"], str):
#         raise ValueError()
#
#     return Item(
#         item_id=data["id"],
#         name=data["name"],
#         price=data["price"],
#         quantity=data["quantity"]
#     )