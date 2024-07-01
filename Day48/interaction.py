from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

no_of_article = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# no_of_article.click()


all_portals = driver.find_element(By.LINK_TEXT, value="View source")
# all_portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("anjesh kumar")
search.send_keys(Keys.ENTER)
# driver.quit()