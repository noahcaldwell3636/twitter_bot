from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import unittest 
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

# access driver as 'chrome_driver'
chrome_driver = webdriver.Chrome(options=options)

chrome_driver.implicitly_wait(2)

chrome_driver.get("https://www.twitter.com")

print("step 1")
try:
    login_button = chrome_driver.find_element(By.LINK_TEXT, 'Log in')
    login_button.click()
except Exception:
    try:
        print("trying other button")
        login_button = chrome_driver.find_element(By.LINK_TEXT, 'Sign in')
        login_button.click()
    except:
        pass


print("step 2")
username_input = chrome_driver.find_element(By.NAME, "text")
username_input.click()
username_input.send_keys("boonedevart\ue007")
# next_button = chrome_driver.find_element(By.XPATH, "//span[(@class='css-901oao') and (@class = 'r-qvutc0')]")
# next_button.click()

try:
    username_input = chrome_driver.find_element(By.NAME, "text")
    username_input.click()
    username_input.send_keys("8048145153\ue007")
except:
    pass

password_input = chrome_driver.find_element(By.NAME, "password")
password_input.click()
password_input.send_keys("tZNSLcEVHhHj88.\ue007")

explore_button = chrome_driver.find_element(By.XPATH, '//a[@href="'+"/explore"+'"]')
explore_button.click()

search_bar = chrome_driver.find_element(By.XPATH, '//input[@placeholder="'+"Search Twitter"+'"]')
search_bar.click()
search_bar.send_keys("@boonedev_\ue007")

html_page = chrome_driver.find_element(By.TAG_NAME, 'html')

action = "like"

for loop_num in range(20):
    like_buttons = chrome_driver.find_elements(By.XPATH, '//div[@data-testid="'+action+'"]')
    for button in like_buttons:
        #coordinates = button.location_once_scrolled_into_view # returns dict of X, Y coordinates
        #print(coordinates)
        #chrome_driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        try:
            button.click()
        except:
            print("could find the button")
            pass
        time.sleep(.2)
    html_page.send_keys(Keys.END)
    
    print(f"\n ending loop number {loop_num} \n")