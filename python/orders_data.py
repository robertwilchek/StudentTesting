# orders_data.py
from typing import List, Dict, Any

Order = Dict[str, Any]
ORDERS: List[Order] = [
    {"id": 101, "total": 29.99, "created": "2025-01-15T09:30:00", "customer": {"first": "Ana", "last": "Zhang"}},
    {"id": 102, "total": 120.00, "created": "2025-01-14T16:10:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 103, "total": 120.00, "created": "2025-01-14T08:05:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 104, "total": 75.50, "created": "2025-01-13T12:00:00", "customer": {"first": "Cara", "last": "Lopez"}},
]