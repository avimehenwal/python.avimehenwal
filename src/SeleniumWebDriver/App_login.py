#ScriptName : App_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://server.corp.avertlabs.internal/"
username = "avimehenwal"
password = "Sample@123"

xpaths = { 'usernameTxtBox' : "//input[@id='MainContent_LoginUser_UserName']",
           'passwordTxtBox' : "//input[@id='MainContent_LoginUser_Password']",
           'submitButton' :   "//input[@id='MainContent_LoginUser_LoginButton']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

try:
    span = mydriver.find_element_by_id("LoginName")
except:
    print("ERROR: mydriver.find_element_by_id")
print(span)
print(span.text)
print(span.get_attribute('value'))