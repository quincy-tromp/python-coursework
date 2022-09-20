from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

USERNAME = os.environ['YOUR_USERNAME']
PASSWORD = os.environ['YOUR_PASSWORD']

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3237822372&geoId=100467493&keywords=data%20engineer&location=Rotterdam%2C%20South%20Holland%2C%20Netherlands&refresh=true")

time.sleep(3)

login_link = driver.find_element(by="link text", value="Sign in")
login_link.click()

time.sleep(2)

email_field = driver.find_element(by="id", value="username")
password_field = driver.find_element(by="id", value="password")
email_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(2)

jobs = driver.find_elements(by="link text", value="Data Engineer")
print(f"{len(jobs)} jobs found")

for number, job in enumerate(jobs, start=1):
    job.click()

    time.sleep(1)

    save_button = driver.find_element(by="class name", value="jobs-save-button")
    save_button.click()
    print(f"job {number} saved")

driver.quit()