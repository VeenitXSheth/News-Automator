import requests
from bs4 import BeautifulSoup
import random

from main import articleURL

print("from scrape.py:", articleURL)

article_request = requests.get(articleURL)

soup = BeautifulSoup(article_request.content, "html.parser")

content_pre_stitched = []

articleTitle = []
articleAuthor = []


def get_content():
    print("getting content!")
    titles = soup.find_all("h1", class_="article__title")
    for title in titles:
        articleTitle.append(title.text)
    authors = soup.find_all("div", class_="article__byline")
    for author in authors:
        articleAuthor.append(author.text)
    content = soup.find_all("div", "article-content")
    for pieces in content:
        content_pre_stitched.append(pieces.text)


get_content()

content = "".join(content_pre_stitched)

print("current article content:", content)
print("current article title:", articleTitle[0])
print("current article author:", articleAuthor[0])
