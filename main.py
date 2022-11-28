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
actions = ActionChains(browser)

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
    time.sleep(2)
    #Select phone number text field
    browser.find_element(By.XPATH,"//span[(contains(., 'Phone') or contains(., 'phone')) and not(contains(., 'country'))]").click() 
    time.sleep(3)
    #Type into phone number text field
    actions.send_keys('111-111-1111')
    actions.perform()
    #Click next
    try:    
        browser.find_element(By.XPATH,"//button[@aria-label='Continue to next step']").click()
    except:
        print("Not found")
        exitApplication()
    exitApplication()
    time.sleep(3)
    
#Exit the job application (Used when application is not supported)
def exitApplication():
    browser.find_element(By.XPATH,"//li-icon[@class='artdeco-button__icon' and @type='cancel-icon']").click()
    time.sleep(2)
    browser.find_element(By.XPATH,"//span[contains(., 'Discard')]").click() 


def checkExperience():
    try:
        el = browser.find_element((By.XPATH,"//button[phone(string(), 'phone')]"))
        actions.move_to_element_with_offset(el,10,10)
        actions.click()
        actions.perform()
    except:
        print('Item not found')
    

def main():
    #Open linkedin.com
    browser.get('http://www.linkedin.com')
    login()
    filterJobs()
    time.sleep(1)
    
    #List of jobs
    listings = browser.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
    #Iterate through each job
    x= 0 #Number of listings to go through
    
    #Go through 50 listings
    while(x < 50):
        for listing in listings:
            listing.click()
            applyToJob()
            time.sleep(2)
        #Update url to load new job listings
        x += 10
        browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3360953405&geoId=103644278&keywords=software%20engineer&location=United%20States&refresh=true&start="+str(x))
        time.sleep(4)
        listings = browser.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
    
            
    #applyToJob()
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    main()
    