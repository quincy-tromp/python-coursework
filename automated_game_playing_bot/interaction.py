from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by="css selector", value="#articlecount a")
print(article_count.text)

# Clicking on button/anchor tag
# article_count.click()

# Finding element by link text and clicking it.
# all_portals = driver.find_element(by="link text", value="All portals")
# all_portals.click()

# Typing in the search bar
search_bar = driver.find_element(by="name", value="name")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

driver.quit()