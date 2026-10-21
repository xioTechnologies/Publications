import xml.etree.ElementTree as ET
from collections import Counter

from publication import read_publications

publications = read_publications("publications.json")

ignore = read_publications("ignore.json")

for publication in [p for p in publications if publications.count(p) > 1]:
    print(f"Duplicate: {publication.title}")

for publication in [p for p in publications if [q.doi for q in publications].count(p.doi) > 1]:
    print(f"Duplicate DOI: {publication.title}")

for publication in [p for p in publications if "NA" in [p.venue, p.year, p.doi, p.product]]:
    print(f"NA: {publication.title}")

for publication in [p for p in publications if p.product not in ["x-IMU", "x-BIMU", "x-OSC", "NGIMU", "x-IMU3"]]:
    print(f"Invalid product: {publication.title}")

for publication in [p for p in publications if len(p.tags) == 0]:
    print(f"No tags: {publication.title}")

for publication in [p for p in ignore if p.comment == ""]:
    print(f"No comment: {publication.title}")

publications = sorted(publications, key=lambda publication: (-int(publication.year), publication.title.lower()))

root = ET.Element("publications", {"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"})

tags = ET.SubElement(root, "tags")

for tag in sorted({t for p in publications for t in p.tags}, key=str.lower):
    ET.SubElement(tags, "tag").text = tag

for publication in publications:
    paper = ET.SubElement(root, "paper")

    ET.SubElement(paper, "author").text = publication.authors
    ET.SubElement(paper, "title").text = publication.title
    ET.SubElement(paper, "venue").text = publication.venue
    ET.SubElement(paper, "year").text = publication.year
    ET.SubElement(paper, "doi").text = publication.doi
    ET.SubElement(paper, "product").text = publication.product

    paper_tags = ET.SubElement(paper, "tags")

    for tag in sorted(publication.tags, key=str.lower):
        ET.SubElement(paper_tags, "tag").text = tag

tree = ET.ElementTree(root)

ET.indent(tree, space="\t", level=0)

tree.write("Publications.xml", encoding="UTF-8", xml_declaration=True)

for product, count in sorted(Counter(p.product for p in publications).items(), key=lambda item: (-item[1], item[0])):
    print(f"{count:<8}{product}")

citations = sum(
    (
        3225,  # Madgwick algorithm: "Estimation of IMU and MARG orientation using a gradient descent algorithm"
        1474,  # Madgwick algorithm: "An efficient orientation filter for inertial and inertial/magnetic sensor arrays"
        len([p for p in ignore if p.product == "Algorithm"]),
        len(publications),
    )
)

institutions = 300  # Claude estimate from publications with allowance for customers who have not published

print(f"{citations:<8}Citations of x-io algorithms and products")
print(f"{len(publications):<8}Published research projects using x-io products")
print(f"{institutions:<8}Research institutions using x-io products")
