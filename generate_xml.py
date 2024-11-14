import xml.etree.ElementTree as ET
from publication import read_publications

publications = read_publications("publications.json")

for index, publication in enumerate(publications):
    if "TODO" in [publication.doi, publication.product]:
        raise Exception(f'"TODO" for index {index}: "{publication.title}"')

    if "NA" in [publication.year, publication.publication]:
        raise Exception(f'"NA" for index {index}: "{publication.title}"')

publications = sorted(publications, key=lambda publication: int(publication.year), reverse=True)

root = ET.Element("publications", {"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"})

for publication in publications:
    paper = ET.SubElement(root, "paper")

    ET.SubElement(paper, "author").text = publication.authors
    ET.SubElement(paper, "title").text = publication.title
    ET.SubElement(paper, "publication").text = publication.publication
    ET.SubElement(paper, "year").text = publication.year
    ET.SubElement(paper, "doi").text = publication.doi
    ET.SubElement(paper, "product").text = publication.product

tree = ET.ElementTree(root)

ET.indent(tree, space="\t", level=0)

tree.write("Publications.xml", encoding="UTF-8", xml_declaration=True)
