from bs4 import BeautifulSoup

page = open("Chap09_test.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())

# print(soup.find_all("p", class_="outer-text"))

# print(soup.find_all("p", attrs={"class": "outer-text"}))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)

