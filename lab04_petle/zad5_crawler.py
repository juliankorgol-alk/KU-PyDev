# Lab 04 – Zadanie 5 (☆, dodatkowe): Mini-crawler
#
# Crawler (robot sieciowy) przegląda strony i zbiera z nich linki.
# Przeczytaj plik dane/strona.html i:
#   1. policz wszystkie linki – wystąpienia tekstu  href="
#   2. wypisz domeny linków bez powtórzeń, np. docs.python.org
#
# Wynik:
#     Liczba linków: 5
#     www.python.org
#     docs.python.org
#     ...
#
# Wskazówki:
#   - text.find('href="', start) zwraca pozycję albo -1 – szukaj w pętli while
#   - adres kończy się na kolejnym znaku "
#   - domena to fragment między "://" a pierwszym "/" po nim
#   - (dla chętnych) urllib.request.urlopen pobierze prawdziwą stronę

with open("dane/strona.html", encoding="utf-8") as f:
    html = f.read()

# TODO: Twój kod poniżej

MARKER = 'href="'

link_count = 0
domains = []
start = 0

while True:
    position = html.find(MARKER, start)
    if position == -1:
        break
    link_count += 1

    url_start = position + len(MARKER)
    url_end = html.find('"', url_start)
    url = html[url_start:url_end]

    scheme_end = url.find("://")
    if scheme_end != -1:
        rest = url[scheme_end + 3:]
        slash = rest.find("/")
        domain = rest if slash == -1 else rest[:slash]
        if domain not in domains:
            domains.append(domain)

    start = url_end + 1

print(f"Liczba linków: {link_count}")
for domain in domains:
    print(domain)
