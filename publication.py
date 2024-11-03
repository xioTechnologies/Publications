import json
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Publication:
    authors: str
    title: str
    publication: str
    year: str
    url: str
    doi: str
    product: str

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()


def read_publications(file_name: str) -> List[Publication]:
    with open(file_name, "r") as file:
        return [Publication(**publication) for publication in json.load(file)]


def write_publications(file_name: str, publications: List[Publication]):
    with open(file_name, "w") as file:
        json.dump([asdict(publication) for publication in publications], file, indent=4)
