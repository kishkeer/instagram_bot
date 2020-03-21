from time import sleep
from selenium import webdriver
import random as rd


class Instabot:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome(r"C:\Users\HP\Desktop\chromedriver.exe")
        #maximize window size
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com")
        sleep(5)
        #username
        login_username=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        login_password=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        submit=self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(5)
    def likes(self):
        #likes the images
        self.driver.find_element_by_class_name('_8-yf5').click()
        sleep(5)
    def scrolling(self):
        SCROLL_PAUSE_TIME = 0.5
        random_number=rd.randint(1,10)

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0,random_number):
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            bot.likes()
            last_height = new_height
    def view_stories(self):
        #duration to stop viewing the status
        stopping_time=rd.randint(30,60)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a').click()
        sleep(stopping_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[3]/div/span').click()
        sleep(5)
    def search(self):
       self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys("#pythonprogramming")
       sleep(2)
       #click_first_result
       self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/span').click()
       sleep(2)

#enter username and password

username=input()
password=input()
#calling_functions

bot=Instabot(username,password)
bot.scrolling()
bot.view_stories()
bot.search()