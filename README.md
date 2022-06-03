# CeneoScraper

## Analiza struktury opinii w serwisie Ceneo.pl

|Składowa|Selektor|Zmienna|Typ zmiennej|
|--------|--------|-------|------------|
|opinia|div.js_product-review|review|bs4.element.Tag|
|identyfikator opinii|\["data-entry-id"\]|review_id|str|
|autor|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|bool|
|liczba gwiazdek|span.user-post__score-count|stars|float|
|treść|div.user-post__text|content|str|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|str|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purcharse_date|str|
|dla ilu przydatna|span[id^=votes-yes]|useful|int|
|dla ilu nieprzydatna|span[id^=votes-no]|useless|int|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros|str|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons|str|

## Etapy pracy nad projektem (wersja strukturalna)

1) pobranie składowych pojedyńczej opinii do niezależnych zmiennych
2) zapisanie wszystkich składowych pojedyńczej opinii do obiektu słownika (dictionary)
3) pobranie wszystkich opinii z pojedyńczej strony i zapisanie ich do listy słowników
4) pobranie wszystkich opinii o wskazanym produkcie i zapisanie ich do pliku
5) Dodanie możliowści podania id produktu przez użytkownika za pomocą klawiatury
6) Refaktoryzacja (optymalizacja) kodu:
    i. utworzenie funkcji do pobierania składowych strony HTML
    ii. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    iii. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe (dictionary comprehension) tworzące słownik reprezentujący  pojedynczą opinię na podstawie słownika selektorów
7) Analiza opinii o wybranym produkcie
    i. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    ii. wyliczenie podstawowych statystyk na podstawie opinii
        a. liczba wszystkich opinii o produkcie
        b. liczba opinii w których autor podał listę zalet produktu
        c. liczba opinii w których autor podał listę wad produktu
        d. średnia ocena produktu
    iii. przygotowanie wykresów na podstawie zawartości opinii
        a. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        b. histogram częstości występowania poszczególnych ocen (liczby gwiazdek)