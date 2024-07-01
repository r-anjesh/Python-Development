from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_title = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(events_title)):
    events[n] = {
        "time" : events_time[n].text,
        "name" : events_title[n].text
    }

print(events)