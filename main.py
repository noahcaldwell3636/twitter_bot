from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import unittest 

# from dotenv import load_dotenv
# load_dotenv()



# try:
#     resume_link = chrome_driver.find_element(By.ID, 'viewer')
# except NoSuchElementException as exception:
#     print(f"could not find pdf viewer element!!! \n {exception}")
# else:
#     print("we found the resume PDF!!!")
    
class TestResumeWebsite(unittest.TestCase):
    
    def setUp(self):
        # gets rid of errors that do not interfere with test execution
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # access driver as 'self.chrome_driver'
        self.chrome_driver = webdriver.Chrome(options=options)
        self.chrome_driver.implicitly_wait(5) # only needs to be called once per session
        

    def test_resume_link(self):
        self.chrome_driver.get("https://www.noahcaldwell.io")
        try:
            resume_button = self.chrome_driver.find_element(By.ID, 'resume_link')
            resume_button.click()
        except Exception as exception:
            print("\n \n There is a problem locating or clicking the resume.pdf button link")
            print(f"\n {exception} \n")
        # Selenium seems to be unable to grab elements in chrome's pdf viewer so a test
        # on the url will have to suffice (as of december 2021)
        assert self.chrome_driver.current_url.__contains__("NoahCaldwell2021Resume.pdf")
        self.chrome_driver.quit()
        
    # def test_resume_pdf(self):
    #     self.chrome_driver.get("https://www.noahcaldwell.io/resume.pdf")
    #     #self.chrome_driver.find_element(By.ID, 'viewer')
    #     #self.chrome_driver.find_element_by_id('viewer')
        
    #     WebDriverWait(self.chrome_driver, 5).until(
    #         expected_conditions.visibility_of_element_located(
    #             #(By.TAG_NAME, 'pdf-viewer')
    #             (By.CSS_SELECTOR, "#viewer")
    #         ) 
    #     )
        
    #     self.chrome_driver.quit()
        

if __name__ == '__main__':
    unittest.main()
    




# r = requests.get("https://www.noahcaldwell.io/resume.pdf")
# print(f"XxXxX {r.status_code} XxXxX")