import ast

from publication import Publication, write_publications

with open("crawl.txt", "r", encoding="utf-8") as file:
    dictionaries = [ast.literal_eval(line.replace("<PublicationSource.PUBLICATION_SEARCH_SNIPPET: 'PUBLICATION_SEARCH_SNIPPET'>", "''")) for line in file]  # remove invalid value

publications = [
    Publication(
        authors=", ".join(dictionary["bib"]["author"]),
        title=dictionary["bib"]["title"],
        venue=dictionary["bib"]["venue"],
        year=dictionary["bib"]["pub_year"],
        url=dictionary["pub_url"],
        doi="NA",
        product="NA",
        tags=[],
        comment="",
    )
    for dictionary in dictionaries
    if "pub_url" in dictionary
]

write_publications("crawl.json", publications)
