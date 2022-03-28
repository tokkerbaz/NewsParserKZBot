import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def check_updates():
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/informburo.json") as file:
        articles = json.load(file)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42"
    }

    url = "https://informburo.kz/novosti"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    article_cards = soup.find_all("li", attrs={'data-day':datetime.now().day})

    fresh_news = {}
    for article in article_cards:
        article_url = article.find('a').get('href')
        article_id = article_url

        if(article_id in articles):
            continue
        else:
            article_title = article.find('a').get_text("|", strip=True)
            article_date = article.attrs['data-date']

            articles[article_id] = {
                "article_date": article_date,
                "article_title" : article_title,
                "article_url": article_url
            }

            fresh_news[article_id] = {
                "article_date": article_date,
                "article_title" : article_title,
                "article_url": article_url
            }

    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/informburo.json", "w") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    check_updates()


if __name__ == '__main__':
    main()



