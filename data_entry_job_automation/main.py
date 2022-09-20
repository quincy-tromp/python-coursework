import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

BASE_URL = "www.pararius.com"
URL = "https://www.pararius.com/apartments/rotterdam/apartment/0-2000"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdsVUtCIIuVGDhrr1B2OS0MiTtaOGvuqYZWa5zJZ4D_RBtZ4g/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "/Applications/chromedriver"

response = requests.get(url=URL)
site_html = response.text
soup = BeautifulSoup(site_html, "html.parser")

search_results = soup.find_all(name="section", class_="listing-search-item")
rental_listings = {}

for index, result in enumerate(search_results, start=1):
    
    address = result.select_one(".listing-search-item__sub-title").get_text().split("(")[0].strip()
    price = result.select_one(".listing-search-item__price").get_text().strip().split()[0].replace(",", "")
    link = BASE_URL + result.select_one(".listing-search-item__link--title").get("href")

    rental_listings[index] = {
        "address": address,
        "price": price,
        "link": link,
    }

def launch_browser():
    driver_service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service)
    driver.get(FORM)
    return driver

driver = launch_browser()

for index, listing in enumerate(rental_listings, 1):
    
    address_form = driver.find_element(by="xpath", 
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form = driver.find_element(by="xpath", 
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form = driver.find_element(by="xpath",
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by="css selector", value="span.NPEfkd")
    
    address_form.send_keys(rental_listings[index]["address"])
    price_form.send_keys(rental_listings[index]["price"])
    link_form.send_keys(rental_listings[index]["link"])
    submit_button.click()

    another_one = driver.find_element(by="link text", value="Nog een antwoord verzenden")
    another_one.click()

print("Processing complete")