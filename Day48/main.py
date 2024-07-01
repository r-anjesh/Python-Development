from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://amzn.in/d/1TxRbNq")


# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f'The Price is {price.text}')
# # close will close single tab
# driver.close()

# search_bar = driver.find_element(By.NAME, value="field-keywords")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# using_selector = driver.find_element(By.CSS_SELECTOR, value=".offers-items-content span")
# print(using_selector.text)


xpath = driver.find_element(By.XPATH, value='//*[@id="customer_review-R1JB3CQAX4TJF4"]/div[4]/span/div/div[1]')
print(xpath.text)
# quit() will close all tabs
driver.quit()

