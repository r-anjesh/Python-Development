from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "*******"
PASSWORD = "********"
SIMILAR_ACCOUNT = 'chefsteps'

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/accounts/login/')


    def login(self):

        time.sleep(3)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        submit = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        submit.click()

        time.sleep(7)
        
        # cancel_notification = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        # cancel_notification.click()


        # self.driver.quit()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        

    def follow(self):
        time.sleep(3)
        all_buttons = self.driver.find_elements(By.XPATH, value="/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]")
        for button in all_buttons:
            try:
                click_follow = button.find_element(By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
                click_follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()
            


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

