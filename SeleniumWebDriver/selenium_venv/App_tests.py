import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   

baseurl = "https://server.corp.avertlabs.internal/"
username = "avimehenwal"
password = "Sample@123"

xpaths = { 'usernameTxtBox' : "//input[@id='MainContent_LoginUser_UserName']",
           'passwordTxtBox' : "//input[@id='MainContent_LoginUser_Password']",
           'submitButton' :   "//input[@id='MainContent_LoginUser_LoginButton']"
         }

class Lyrids(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(baseurl)
    
    def test_title_match(self):        
        self.assertIn("URL ticket submission portal", self.driver.title)

    def test_home_has_form(self):
        # try:
        #     form = driver.find_element_by_tag_name('form')
        # except NoSuchElementException:
        #     print("EXCEPTION : form not found")

        # if form.is_displayed():
        #     print("is visible")
        # else:
        #     print("Not visible")
        # print(driver.find_element(By.TAG_NAME, "form"))
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "form"))

    def test_login(self):
        self.driver.maximize_window()
        #Clear Username TextBox if already allowed "Remember Me" 
        self.driver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
        #Write Username in Username TextBox
        self.driver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
        #Clear Password TextBox if already allowed "Remember Me" 
        self.driver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
        #Write Password in password TextBox
        self.driver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
        #Click Login button
        self.driver.find_element_by_xpath(xpaths['submitButton']).click()
        try:
            span = self.driver.find_element_by_id("LoginName")
        except:
            raise error("cannot find span with ID LoginName")
        # print(span)
        # print(span.get_attribute('value'))
        self.assertEqual(span.text[6:16], username[:10], msg="Username on UI is different than entered")        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()