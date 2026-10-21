from pathlib import Path

from bs4 import BeautifulSoup
from scholarly._navigator import Navigator
from scholarly.data_types import Publication, PublicationSource
from scholarly.publication_parser import PublicationParser

navigator = Navigator()


def parse_page(path: Path) -> list[Publication]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8").replace("\xa0", " "), "html.parser")

    navigator.publib = soup.find("div", id="gs_res_glb").get("data-sva")  # normally set by scholarly when a page is downloaded

    parser = PublicationParser(navigator)

    return [parser.get_publication(row, PublicationSource.PUBLICATION_SEARCH_SNIPPET) for row in soup.find_all("div", class_="gs_r gs_or gs_scl")]


results = [result for path in sorted(Path("html").glob("*.html")) for result in parse_page(path)]

Path("crawl.txt").write_text("".join(f"{result}\n" for result in results), encoding="utf-8")

print(f"{len(results)} results")
