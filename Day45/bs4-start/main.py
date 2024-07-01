from bs4 import BeautifulSoup
# import lxml


with open("./Day45/bs4-start/website.html", 'r', encoding='utf-8') as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

# for tags in all_anchor_tags:
#     print(tags.get("href "))

# heading = soup.find(name="h3", class_ = "heading")
# print(heading.get("n"))

company_url = soup.select_one(selector="p a")
print(company_url.get("href "))
