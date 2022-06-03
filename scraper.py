import json
import selectors
import requests
from bs4 import BeautifulSoup

def get_item(ancestor, selector,attribute=None, return_list=False):
    try:
        if attribute:
            return ancestor.select_one(selector)[attribute]
        elif return_list:
            return [item.text.strip() for item in ancestor.select(selector)]
        else:
            return ancestor.select_one(selector).text.strip()
    except (AttributeError,TypeError): 
        return None

selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "publish_date": ["span.user-post__published > time:nth-child(1)","datetime"],
    "purcharse_date": ["span.user-post__published > time:nth-child(2)","datetime"],
    "useful": ["span[id^=votes-yes]"],
    "useless": ["span[id^=votes-no]"],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True]
}        

product_id = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        single_opinion = {key:get_item(opinion, *values)
                        for key, values in selectors.items()}
        single_opinion["review_id"] = opinion["data-entry-id"]

        all_opinions.append(single_opinion)

    try: 
        url = "https://www.ceneo.pl"+page.select_one("a.pagination__next")["href"]
    except TypeError: url = None    

with open(f"./opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)