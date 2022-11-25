from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time 
import unittest

#Open microsoft edge
browser = webdriver.Edge()
email = "pclass184@gmail.com"
passW = "-Y5bKwD5_QSZNdE"

#Login to website
def login():
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='session_key']")))
    browser.find_element(By.NAME,"session_key").send_keys(email)
    browser.find_element(By.NAME,"session_password").send_keys(passW)
    time.sleep(3)
    browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()
    
def main():
    #Open linkedin.com
    browser.get('http://www.linkedin.com')
    login()
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    main()
    