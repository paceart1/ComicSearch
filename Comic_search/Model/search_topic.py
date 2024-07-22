from dataclasses import dataclass


@dataclass
class SearchTopic:
    id: str
    name: str
    number: str
    era: list
    keywords: list
    grades: list
    exclusions: list
    minprice: float
    maxprice: float
    item_block_list: str
