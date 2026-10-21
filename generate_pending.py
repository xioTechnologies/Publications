from publication import read_publications, write_publications

publications = read_publications("publications.json")

crawl = read_publications("crawl.json")

ignore = read_publications("ignore.json")

pending = [p for p in crawl if (p not in publications) and (p not in ignore)]

write_publications("pending.json", pending)
