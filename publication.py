import json
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from typing import Self


@dataclass
class Publication:
    authors: str
    title: str
    venue: str
    year: str
    url: str
    doi: str
    product: str
    tags: list[str]
    comment: str

    def __eq__(self, other: Self) -> bool:  # type: ignore[override]
        matcher = SequenceMatcher(None, self.title.lower(), other.title.lower())

        return matcher.real_quick_ratio() > 0.9 and matcher.quick_ratio() > 0.9 and matcher.ratio() > 0.9


def read_publications(file_name: str) -> list[Publication]:
    with open(file_name, "r", encoding="utf-8") as file:
        return [Publication(**publication) for publication in json.load(file)]


def write_publications(file_name: str, publications: list[Publication]) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump([asdict(publication) for publication in publications], file, indent=4, ensure_ascii=False)
