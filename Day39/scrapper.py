import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/data-structures"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

dsa = soup.find('h2').text

paragraph = soup.find_all('p')
dsa_answer = (paragraph[2].text + paragraph[3].text)


classification = soup.find(id = "classification-of-data-structure").text
classification_answer = soup.find_all('span')
print(classification_answer[19].text)
# print(dsa + "\n" + dsa_answer + "\n" + classification + "\n" + classification_answer[10].text)

