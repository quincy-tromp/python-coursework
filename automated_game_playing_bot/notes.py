# from selenium import webdriver

# chrome_driver_path = "/Applications/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # url = "https://www.amazon.nl/Instant-Pot-elektrische-sterilisator-graandecoratie/dp/B08Z4GVY54/ref=sr_1_5?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1C6RSBEWUT18Z&keywords=instant+pot&qid=1662231560&sprefix=instant+pot%2Caps%2C86&sr=8-5"
# # driver.get(url=url)
# # price = driver.find_element(by="class name", value="a-price-whole")
# # print(price.text)

# # search_bar = driver.find_element(by="id", value="nav-search-bar-form")
# # print(search_bar.tag_name)

# # # driver.close() 
# # driver.quit()
# # What's the difference between close() and quit() ?
# # Closes a single tab (the active tab)
# # Quits the entire browser

# driver.get("https://www.python.org/")

# event_times = driver.find_elements(by="css selector", value=".event-widget time")
# event_names = driver.find_elements(by="css selector", value=".event-widget li a")
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
# print(events)

# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by="name", value="fName")
first_name.send_keys("Quincy")
last_name = driver.find_element(by="name", value="lName")
last_name.send_keys("Tester")
email = driver.find_element(by="name", value="email")
email.send_keys("quincytester@gmail.com")

submit = driver.find_element(by="tag name", value="button")
submit.click()
