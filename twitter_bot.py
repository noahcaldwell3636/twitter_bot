from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import unittest 


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

like_buttons = chrome_driver.find_elements(By.XPATH, '//svg[@viewbox="'+"0 0 24 24"+'"]')


# <svg viewBox="0 0 24 24" aria-hidden="true" 
# class="r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi">
# <g><path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754
# 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.037
# 13.157H12zM7.354 4.225c-2.08 0-3.903 1.988-3.903 4.255 0 5.74 7.034 11.596 8.55 11.658 1.518-.062 8.55-5.917 8.55-11.658
# 0-2.267-1.823-4.255-3.903-4.255-2.528 0-3.94 2.936-3.952 2.965-.23.562-1.156.562-1.387 0-.014-.03-1.425-2.965-3.954-2.965z">
# </path></g></svg>