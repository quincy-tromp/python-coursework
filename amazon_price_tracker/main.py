import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.nl/Instant-Pot-elektrische-sterilisator-graandecoratie/dp/B08Z4GVY54/ref=sr_1_5?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1C6RSBEWUT18Z&keywords=instant+pot&qid=1662231560&sprefix=instant+pot%2Caps%2C86&sr=8-5"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Langauge": "en-US,en;q=0.9,nl;q=0.8,es;q=0.7",
}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(id="priceblock_outprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
#print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}"
        )