from publication import read_publications, write_publications

publications = read_publications("publications.json")

crawl = read_publications("crawl.json")

ignore = read_publications("ignore.json")

pending = [p for p in crawl if (p not in publications) and (p not in ignore)]

write_publications("pending.json", pending)

with open("pending.html", "w", encoding="utf-8") as file:
    file.write("<!DOCTYPE html><html><head>")
    file.write("<style>table{border-spacing:0;width:100%;border:1pxsolid #ddd;}th,td{text-align:left;padding:4px;}tr:nth-child(even){background-color:#f2f2f2}</style>")
    file.write('</head><body><table style="width:100%"><tr>')
    file.write("<th>Row</th>")
    file.write("<th>Authors</th>")
    file.write("<th>Title</th>")
    file.write("<th>Publication</th>")
    file.write("<th>Year</th>")
    file.write("<th>URL</th>")
    file.write("</tr>\n")

    row = 0

    for publication in pending:
        row += 1

        file.write("<tr>")
        file.write(f"<td>{str(row)}</td>")
        file.write(f"<td>{publication.authors}</td>")
        file.write(f"<td>{publication.title}</td>")
        file.write(f"<td>{publication.publication}</td>")
        file.write(f'<td><a href="{publication.url}" target="_blank">{publication.url}</a></td>')
        file.write("</tr>\n")

    file.write("</table></body></html>")
