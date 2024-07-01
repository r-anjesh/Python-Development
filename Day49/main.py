# LINKEDIN EASY SAVE/APPLY JOBS


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "hide@gmail.com"
PASSWORD = "@pass"


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3855110074&distance=25&f_AL=true&f_WT=2%2C1%2C3&geoId=104869687&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

sign_in = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

username = driver.find_element(By.XPATH, value='//*[@id="username"]')
username.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys(PASSWORD)

login = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login.send_keys(Keys.ENTER)
time.sleep(3)
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, value='.jobs-search-results-list ul li')

