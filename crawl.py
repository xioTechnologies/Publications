from scholarly import scholarly

# WARNING: Google Scholar will stop responding if you run this too many times

results = scholarly.search_pubs('"x-io Technologies"')

with open("crawl.txt", "w", encoding="utf-8") as file:
    for result in results:
        print(result)

        file.write(str(result) + "\n")
