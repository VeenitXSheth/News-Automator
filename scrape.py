import requests
from bs4 import BeautifulSoup
import random
import colorama
from colorama import Fore

from main import articleURL

article_request = requests.get(articleURL)

soup = BeautifulSoup(article_request.content, "html.parser")

content_pre_stitched = []

articleTitle = []
articleAuthor = []


def get_content():
    titles = soup.find_all("h1", class_="article__title")
    for title in titles:
        articleTitle.append(title.text)
    authors = soup.find_all("div", class_="article__byline")
    for author in authors:
        authorRemoveOne = author.text.replace("\n", "")
        authorRemoveTwo = authorRemoveOne.replace("\t", "")
        articleAuthor.append(authorRemoveTwo)
    content = soup.find_all("div", "article-content")
    for pieces in content:
        content_pre_stitched.append(pieces.text)


get_content()

content = "".join(content_pre_stitched)

file_name = "".join(articleTitle)
authorFormatted = "".join(articleAuthor)
author = authorFormatted.replace("/", "-")

print(Fore.BLUE + "Article Title:", file_name)
print(Fore.GREEN + "Article Content:", content)
print(Fore.MAGENTA + "Article Author:", author, "ago")

with open(f"{file_name}", "w") as f:
    f.write(
        f"""Original Article: {file_name}
Content: {content}
Written By: {author} ago
Link: {articleURL}"""
    )
