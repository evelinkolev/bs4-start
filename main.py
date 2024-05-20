from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_texts = []
article_links = []

news = soup.find_all(class_="titleline")

for heading in news:
    article_texts.append(heading.find(name="a").getText())
    article_links.append(heading.find(name="a").get("href"))

scores = soup.find_all(class_="score")

article_votes = []

for score in scores:
    article_votes.append(int(score.getText().split(" ")[0]))

print(article_texts)
print(article_links)
print(article_votes)