from bs4 import BeautifulSoup
import requests, re

r = requests.get("https://nakedsecurity.sophos.com").content
soup = BeautifulSoup(r, 'html.parser')

hero = soup.findAll("article")

for h in hero:
    a = h.find("span", {"class":"month"})
    text = a.text
    a = h.find("span", {"class":"day"})
    text += a.text
    a = h.find("a", {"rel":"bookmark"})
    text += " "
    text += a.text
    text += " LINK: "
    text += a.get('href')
    print(text)


