from selenium import webdriver
import time 

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id", value="cookie")

store_items = driver.find_elements(by="css selector", value="#store div")
item_ids = [item.get_attribute("id") for item in store_items]

print(time.time())
timeout = time.time() + 5
five_min = time.time() + 60 * 5
print(five_min)

while True:
    cookie.click()
    
    if time.time() > timeout:

        store_items = driver.find_elements(by="css selector", value="#store b")
        item_prices = []

        for item in store_items:
            if item.text != "":
                price = int(item.text.split("-")[1].split("\n")[0].strip().replace(",", ""))
                item_prices.append(price)

        cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}

        money_element = driver.find_element(by="id", value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        money = int(money_element)

        affordable_upgrades = {}
        for price, id in cookie_upgrades.items():
            if money > price:
                affordable_upgrades[price] = id

        highest_affordable_upgrade = max(affordable_upgrades)
        to_buy_id = affordable_upgrades[highest_affordable_upgrade]

        driver.find_element(by="id", value=to_buy_id).click()
    
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_second = driver.find_element(by="id", value="cps").text
        print(time.time())
        print(cookie_per_second)
        break

driver.quit()