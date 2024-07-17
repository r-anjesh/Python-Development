from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_FORM = os.getenv('GOOGlE_FORM')
NAME = os.getenv('NAME')
GENDER = os.getenv('GENDER')
PHONE = os.getenv('PHONE')
EMAIL = os.getenv('EMAIL')
DOB = os.getenv('DOB')
ADDRESS = os.getenv('ADDRESS')
PINCODE = os.getenv('PINCODE')

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open the Google Form
driver.get(GOOGLE_FORM)

# Allow the page to load
time.sleep(2)

# Fill in the form
name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/di'
                                           'v/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys(NAME)

phone_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div'
                                            '[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone_field.send_keys(PHONE)

email_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div'
                                            '/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys(EMAIL)

full_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/'
                                             'div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
full_address.send_keys(ADDRESS)

pincode_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]'
                                              '/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pincode_field.send_keys(PINCODE)

dob_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/d'
                                          'iv[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')

action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(dob_field, 55, 0).click().perform()
time.sleep(1)
dob_field.send_keys(DOB)
gender_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                             'div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender_field.send_keys(GENDER)

code = driver.find_element(By.XPATH, '//*[@id="i30"]/span[1]/b')
code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]'
                                           '/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
code_field.send_keys(code.text)

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()

# Wait for the confirmation page
time.sleep(2)

# Take a screenshot of the confirmation page
driver.save_screenshot('confirmation_page.png')

# Close the browser
driver.quit()
