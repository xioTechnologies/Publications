import ast
from publication import Publication, write_publications

publications = []

with open("crawl.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("<PublicationSource.PUBLICATION_SEARCH_SNIPPET: 'PUBLICATION_SEARCH_SNIPPET'>", "''")  # remove invalid value

        dictionary = ast.literal_eval(line)

        if "pub_url" not in dictionary:
            continue

        publications.append(
            Publication(
                authors=", ".join(dictionary["bib"]["author"]),
                title=dictionary["bib"]["title"],
                publication=dictionary["bib"]["venue"],
                year=dictionary["bib"]["pub_year"],
                url=dictionary["pub_url"],
                doi="TODO",
                product="TODO",
            )
        )

write_publications("crawl.json", publications)
