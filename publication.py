import json
from dataclasses import dataclass, asdict
from difflib import SequenceMatcher
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

    def __eq__(self, other: "Publication"):
        return SequenceMatcher(None, self.title.lower(), other.title.lower()).ratio() > 0.9


def read_publications(file_name: str) -> List[Publication]:
    with open(file_name, "r") as file:
        return [Publication(**publication) for publication in json.load(file)]


def write_publications(file_name: str, publications: List[Publication]):
    with open(file_name, "w") as file:
        json.dump([asdict(publication) for publication in publications], file, indent=4)
