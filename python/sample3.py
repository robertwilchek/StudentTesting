"""Sample script that sorts orders with nested customer data."""

from __future__ import annotations

from datetime import datetime
from pprint import pprint
from typing import List, TypedDict


class Customer(TypedDict):
    first: str
    last: str


class Order(TypedDict):
    id: int
    total: float
    created: str
    customer: Customer


ORDERS: List[Order] = [
    {"id": 101, "total": 29.99, "created": "2025-01-15T09:30:00", "customer": {"first": "Ana", "last": "Zhang"}},
    {"id": 102, "total": 120.00, "created": "2025-01-14T16:10:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 103, "total": 120.00, "created": "2025-01-14T08:05:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 104, "total": 75.50, "created": "2025-01-13T12:00:00", "customer": {"first": "Cara", "last": "Lopez"}},
]


def sort_orders(orders: List[Order]) -> List[Order]:
    """Return orders sorted by customer (last, first) and creation timestamp."""

    def sort_key(order: Order) -> tuple[str, str, datetime]:
        created_at = datetime.fromisoformat(order["created"])
        customer = order["customer"]
        return (customer["last"].lower(), customer["first"].lower(), created_at)

    return sorted(orders, key=sort_key)


if __name__ == "__main__":
    pprint(sort_orders(ORDERS))
