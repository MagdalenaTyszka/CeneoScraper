# CeneoScraper

## Analiza struktury opinii w serwisie Ceneo.pl

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|review|
|Identyfikator opinii|\[(data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recomendation|
|liczba gwiazdek|span.user-post__score-count|stars|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post_published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post_published > time:nth-child(2)\[datetime\]|purcharse_date|
|dla ilu przydatna|span[id^votes-yes]|useful|
|dla ilu nieprzydatna|span[id^votes-no]|useless|
|lista zalet|div.review-feature_title--positives ~ review-feature_item|adv|
|lista wad|div.review-feature_title--negatives ~ review-feature_item|dis|