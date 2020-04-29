from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time

CONFIGS = {
    'USERNAME': input("username:"),
    'PASSWORD': input("password:"),
    'HASHTAGS': [ 'love', 'cars'],
    'TOTAL_LIKES_PER_HASHTAG':10,

}

total_likes = 0
total_follows=0

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\chromedriver.exe')#enter the path of chromedriver
driver.get("https://www.instagram.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((   By.NAME, 'username')))
usernameInput = driver.find_element(By.NAME, 'username')
usernameInput.send_keys(CONFIGS['USERNAME'])

passwordInput = driver.find_element(By.NAME, 'password')
passwordInput.send_keys(CONFIGS['PASSWORD'])

passwordInput.submit()

# Search
WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")))

for current_hashtag in CONFIGS['HASHTAGS']:
    driver.get("https://www.instagram.com/explore/tags/{}/".format(current_hashtag) )
     # Search results
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    print("Loaded #{}".format(current_hashtag))

    results = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

    if not results:
        print("No results for #{}".format(current_hashtag))
        driver.quit()

    print("Opening first post from #{}...".format(current_hashtag))
    results[0].click()

    current_hashtag_likes = 0
    current_follows=0
   while current_hashtag_likes < CONFIGS['TOTAL_LIKES_PER_HASHTAG']:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "time")))
        time.sleep(1)
        likeButton = driver.find_element(By.XPATH,
                                         "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        likeButton.click()
        time.sleep(3)

        follower = driver.find_element(By.XPATH,
                                       "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
        if follower.text == "Follow":
           follower.click()
           total_follows = total_follows + 1
           current_follows = current_follows + 1
        time.sleep(3)

        print("[#{}/{}/{}/no of follows:{}]".format(
            current_hashtag,
            current_hashtag_likes,
            CONFIGS['TOTAL_LIKES_PER_HASHTAG'],
            current_follows
        ))

        total_likes = total_likes + 1
        current_hashtag_likes = current_hashtag_likes + 1

        time.sleep(10)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'coreSpriteRightPaginationArrow')))

        nextButton = driver.find_element(By.CLASS_NAME, 'coreSpriteRightPaginationArrow')

        nextButton.click()

print("Exiting...")
print("=====================")
print("Total posts liked: {}".format(total_likes))
print("Total follows:{}".format(total_follows))
driver.quit()
