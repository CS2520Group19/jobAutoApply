from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time 
import unittest
from selenium.webdriver.common.action_chains import ActionChains


#Open microsoft edge
browser = webdriver.Edge()
browser.maximize_window()
email = "pclass184@gmail.com"
passW = "-Y5bKwD5_QSZNdE"

#Login to website
def login():
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='session_key']")))
    browser.find_element(By.NAME,"session_key").send_keys(email)
    browser.find_element(By.NAME,"session_password").send_keys(passW)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()

#Filter jobs by easy apply
def filterJobs():
    browser.get("https://www.linkedin.com/jobs/search/")
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']")))
    browser.find_element(By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']").click()
    
def applyToJob():
    time.sleep(2)
    #Find apply button
    browser.find_element(By.XPATH,"//div[@class='jobs-apply-button--top-card']").click()
    time.sleep(1)
    #Select phone number text field
    browser.find_element(By.XPATH,"//div[@class='display-flex']").click()
    time.sleep(3)
    #Type into phone number text field
    actions = ActionChains(browser)
    actions.send_keys('111-111-1111')
    actions.perform()
    #Click next
    browser.find_element(By.XPATH,"//button[@aria-label='Continue to next step']").click()
    
    
    

def main():
    #Open linkedin.com
    browser.get('http://www.linkedin.com')
    login()
    filterJobs()
    applyToJob()
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    main()
    