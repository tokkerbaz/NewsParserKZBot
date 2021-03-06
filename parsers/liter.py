import json
import os
import requests
from bs4 import BeautifulSoup

def check_updates():
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/liter.json") as file:
        articles = json.load(file)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42"
    }

    url = "https://liter.kz/news/all/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    article_cards = soup.find_all("div", class_="news--border-bottom")
    
    fresh_news = {}
    for article in article_cards:
        if len(article.find_all('a')) >=1: 
            article_url = f"https://liter.kz{article.find('a', class_='news__link').get('href')}"
            article_id = (article_url.split("/")[-2]).split("-")[-1]

            if(article_id in articles):
                continue
            else:
                article_title = json.dumps(article.find('a', class_='news__link').text.strip())
                article_date = article.find("div", class_='news__date').text.strip()

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

    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/liter.json", "w") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    check_updates()


if __name__ == '__main__':
    main()



