from publication import read_publications, write_publications

for file_name in ["crawl.json", "pending.json", "ignore.json", "publications.json"]:
    publications = read_publications(file_name)

    publications = sorted(publications, key=lambda publication: (publication.title.lower(), publication.url))

    write_publications(file_name, publications)
