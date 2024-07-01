# Amazon Price Tracker


import requests
# import lxml
from bs4 import BeautifulSoup
import smtplib

EMAIL = "email@gmail.com"
PASSWORD = "pass"



AMAZON_URL = "https://www.amazon.in/Samsung-25W-Travel-Adapter/dp/B08VFF6JQ8/ref=lp_1389401031_1_3?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=B1T4QAVQGPGG7JWWCASV&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&th=1"
HEADER = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,mr;q=0.6"
}

response = requests.get(url=AMAZON_URL, headers= HEADER)

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-price-whole").getText()


title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 1000

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )




