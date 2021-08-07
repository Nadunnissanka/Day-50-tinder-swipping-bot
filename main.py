from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

PHONE_NUMBER = "0756790646"
PASSWORD = "Nadun123@"

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(5)
cookie_accept = driver.find_element_by_xpath('//*[@id="s722988905"]/div/div[2]/div/div/div[1]/button')
cookie_accept.click()

time.sleep(2)
# clicking on get started button
get_started = driver.find_element_by_xpath(
    '//*[@id="s722988905"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
get_started.click()

time.sleep(3)
# click on login with google
facebook_login = driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()

# Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# phone number input
time.sleep(2)
facebook_user_number = driver.find_element_by_xpath('//*[@id="email"]')
facebook_user_number.send_keys(PHONE_NUMBER)
time.sleep(1)
facebook_password = driver.find_element_by_xpath('//*[@id="pass"]')
facebook_password.send_keys(PASSWORD)
time.sleep(1)
facebook_password.send_keys(Keys.ENTER)

# Switch to Facebook login window
time.sleep(1)
driver.switch_to.window(base_window)
print(driver.title)

# enable location
time.sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
time.sleep(3)
allow_notification = driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div/div/div[3]/button[1]')
allow_notification.click()
time.sleep(10)

# fetch like button
swipping_on = True
count = 0
a = 0
# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            f'//*[@id="s722988905"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[{a}]/div/div[4]/button')
        a = 5
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
