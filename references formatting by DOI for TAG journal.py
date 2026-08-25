#The python script I used for formatting references for the Theoretical and Applied Genetics journal

import requests


def get_metadata_from_doi(doi):
    """Получает метаданные статьи по DOI."""
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url, headers={"Accept": "application/json"})
    if response.status_code == 200:
        data = response.json()
        authors = []
        for author in data["message"].get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            formatted_name = f"{family} {given[0]}" if given else family
            authors.append(formatted_name)
        year = (
            data["message"]
            .get("published-print", data["message"].get("published-online", {}))
            .get("date-parts", [[None]])[0][0]
        )
        title = data["message"].get("title", [""])[0]
        journal = data["message"].get("container-title", [""])[0]
        volume = data["message"].get("volume", "")
        issue = data["message"].get("issue", "")
        pages = data["message"].get("page", "")
        return authors, year, title, journal, volume, issue, pages, doi
    else:
        print("Ошибка при получении данных. Проверьте DOI.")
        return None


def format_reference(authors, year, title, journal, volume, issue, pages, doi):
    """Форматирует библиографическую ссылку."""
    authors_str = ", ".join(authors)
    issue_str = f"({issue})" if issue else ""
    pages_str = f":{pages}" if pages else ""
    return f"{authors_str} ({year}) {title}. {journal} {volume}{issue_str}{pages_str}. https://doi.org/{doi}"


doi = input("Введите DOI: ")
metadata = get_metadata_from_doi(doi)
if metadata:
    formatted_reference = format_reference(*metadata)
    print("\nСформированная ссылка:")
    print(formatted_reference)
