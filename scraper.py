import json
import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/61777651#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("div.js_product-review")

all_reviews = []

for review in reviews:

    review_id = review["data-entry-id"]
    author = review.select("span.user-post__author-name").pop(0).text.strip()

    try:
        recommendation = review.select("span.user-post__author-recomendation > em").pop(0).text
        recommendation = True if recommendation == "Polecam" else False 
    except: recommendation = None

    stars = review.select("span.user-post__score-count").pop(0).text
    stars = float(stars.split("/").pop(0).replace(",","."))

    content = review.select("div.user-post__text").pop(0).get_text()
    content = content.replace("\n"," ").strip()

    publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]
    publish_date = publish_date.split(" ").pop(0)

    try:
        purcharse_date = review.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"]
        purcharse_date = purcharse_date.split(" ").pop(0)
    except IndexError:  purcharse_date = None   

    useful = review.select("span[id^=votes-yes]").pop(0).text
    useful = int(useful)

    useless = review.select("span[id^=votes-no]").pop(0).text
    useless = int(useless)

    pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
    pros = [item.text.strip() for item in pros]
    pros = ", ".join(pros)

    cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
    cons = [item.text.strip() for item in cons]
    cons = ", ".join(cons)

    single_review = {
        "review_id": review_id,
        "author": author,
        "recommendation": recommendation,
        "stars": stars,
        "content": content,
        "publish_date": publish_date,
        "purcharse_date": purcharse_date,
        "useful": useful,
        "useless": useless,
        "pros": pros,
        "cons": cons
    }
    all_reviews.append(single_review)

    print(json.dumps(all_reviews, indent=4, ensure_ascii=False))