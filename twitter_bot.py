# selenium imports
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# other
import time

#################__SETUP_ENVIRONMENT_VARIABLES#################################
if __name__ == '__main__':
    from dotenv import dotenv_values
    try:
        config = dotenv_values(".env")
        USERNAME = config['USERNAME']
        PHONENUMBER = config['PHONENUMBER']
        PASSWORD = config['PASSWORD']
        TARGET_ACCOUNT = config['TARGET_ACCOUNT']
    except:
        print("the .env file either does not exist, or does not have"
            "the USERNAME, PHONENUMBER, PASSWORD, or TARGET_ACCOUNT"
            "properly assigned.")
####################END_ENVIRONMENT_VARIABLES_SETUP#############################



################################################################################
##########################____FUNCTIONS____#####################################
################################################################################ 



def chrome_driver_setup(
    implicit_wait_time=2,
    supress_warnings_in_output=True,
    keep_browser_open=True,
    
):
    options = webdriver.ChromeOptions()
    # reduce logging output
    if supress_warnings_in_output: 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # close browser at end of execution... or leave it open
    if keep_browser_open:
        options.add_experimental_option("detach", True)
    # create seleniums chrome driver object
    chrome_driver = webdriver.Chrome(options=options)
    # how many seconds the script will wait to find an element
    chrome_driver.implicitly_wait(implicit_wait_time)
    return chrome_driver

def _press_login():
    try:
        login_button = chrome_driver.find_element(By.LINK_TEXT, 'Log in')
        login_button.click()
    except Exception:
        try:
            login_button = chrome_driver.find_element(By.LINK_TEXT, 'Sign in')
            login_button.click()
        except:
            pass
        
def _enter_username():
    username_input = chrome_driver.find_element(By.NAME, "text")
    username_input.click()
    username_input.send_keys(USERNAME + Keys.ENTER)
    
def _enter_phone_number():
    # if prompted, enter phone number
    try:
        username_input = chrome_driver.find_element(By.NAME, "text")
        username_input.click()
        username_input.send_keys(PHONENUMBER + Keys.ENTER)
    except:
        pass

def _enter_password():
    password_input = chrome_driver.find_element(By.NAME, "password")
    password_input.click()
    password_input.send_keys(PASSWORD + Keys.ENTER)

def twitter_login():
    # open twitter 
    chrome_driver.get("https://www.twitter.com")
    _press_login()
    _enter_username()
    _enter_phone_number()
    _enter_password()

def search_target_user():
    # hit search button (magnify glass icon)
    explore_button = chrome_driver.find_element(
        By.XPATH, '//a[@href="'+"/explore"+'"]') 
    explore_button.click()
    # search username that you want to give likes to
    search_bar = chrome_driver.find_element(
        By.XPATH, '//input[@placeholder="'+"Search Twitter"+'"]')
    search_bar.click()
    search_bar.send_keys("@" + TARGET_ACCOUNT + Keys.ENTER)

def like_posts_found():
    # find buttons on page
    like_buttons = chrome_driver.find_elements(
        By.XPATH, '//div[@data-testid="like"]')
    buttons_found = len(like_buttons)
    successful_likes = 0
    # press all found like buttons
    for button in like_buttons:
        try:
            button.click()
            successful_likes += 1
        except:
            # just skip button if it gets lost
            # or changed so script can continue
            print("Bot could find the button.")
            pass
        # short wait time to prevent errors from
        # any lag on twitter's webpage
        time.sleep(.2)
    print(f"{successful_likes} of {buttons_found}"
          " were completed.")
    
        
        
        
################################################################################
##########################___END_FUNCTIONS____##################################
################################################################################



########################__MAIN_EXECUTION__######################################

if __name__ == '__main__':
    # create selenium chrome object
    chrome_driver = chrome_driver_setup()
    twitter_login()
    search_target_user()
    # like all unliked posts that show up on the search results
    html_page = chrome_driver.find_element(By.TAG_NAME, 'html')
    while True:
        like_posts_found()
        # move page down to avoid stale element errors
        #html_page.send_keys(Keys.END)