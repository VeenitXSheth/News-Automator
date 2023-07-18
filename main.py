import requests
from bs4 import BeautifulSoup
import random

urls = {
    "startups": "https://techcrunch.com/category/startups/",
    "venture": "https://techcrunch.com/category/venture/",
    "security": "https://techcrunch.com/category/security/",
    "ai": "https://techcrunch.com/category/artificial-intelligence/",
    "crypto": "https://techcrunch.com/category/crypto/",
    "apps": "https://techcrunch.com/category/apps/",
}

scraping_url = random.choice(list(urls.values()))

print("The URL chosen:", scraping_url)

initial_request = requests.get(scraping_url)

soup = BeautifulSoup(initial_request.content, "html.parser")

articles = []


def scrape():
    print("A scrape has started!")
    titles = soup.find_all("a", class_="post-block__title__link")
    for title in titles:
        articles.append(title["href"])


scrape()

chosen_topic = random.choice(articles)
print("Chosen article URL:", chosen_topic)

articleURL = chosen_topic
