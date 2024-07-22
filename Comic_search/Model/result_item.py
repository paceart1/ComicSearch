from dataclasses import dataclass

@dataclass
class ResultItem:
    id: str
    description: str
    price: float
    shipping: float
    time: str

