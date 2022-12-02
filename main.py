from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time 
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import traceback



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
    browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3383345613&geoId=103644278&keywords=franklin%20fitch%20system%20engineer&location=United%20States&refresh=true@start=5")
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']")))
    browser.find_element(By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']").click()
    
def applyToJob():
    time.sleep(2)
    #Find apply button
    browser.find_element(By.XPATH,"//div[@class='jobs-apply-button--top-card']").click()
    time.sleep(2)
    #Select phone number text field
    browser.find_element(By.XPATH,"//span[(contains(., 'Phone') or contains(., 'phone')) and not(contains(., 'country'))]").click() 
    time.sleep(1)
    #Type into phone number text field
    for i in range(10):
        actions.send_keys(Keys.BACKSPACE)
        actions.perform()
    actions.send_keys('111-111-1111')
    actions.perform()
    #Check to see if application is simple (Only need to hit submit button)
    submitButton = browser.find_elements(By.XPATH,"//button[@aria-label='Submit application']")
    if len(submitButton) > 0:
        submitButton[0].click() #commented out so application is not sent for test run
        time.sleep(2)
        browser.find_element(By.XPATH,"//li-icon[@type='cancel-icon' and @class='artdeco-button__icon']").click()
        return
    
    try:    
        browser.find_element(By.XPATH,"//button[@aria-label='Continue to next step']").click()
    except:
        print("Next Failed.")
    # #Click next
    resumeScreen = browser.find_elements(By.XPATH,"//h3[contains(., 'Resume') and @class='t-16 t-bold']")
    #If simple resume screen hit next
    if len(resumeScreen) > 0:
        try:    
            browser.find_element(By.XPATH,"//button[@aria-label='Continue to next step']").click()
        except:
            print("Check resume screen failed.")
        time.sleep(1)
    
    submitted = False
    iterations = 0
    while submitted == False and iterations < 4:
        try:
            submitted = nextButton()
            print(submitted)
            iterations += 1
            print(iterations)
        except:
            print("next button exception in method ApplyToJob()")
    exitApplication()
    time.sleep(3)
    
def nextButton():

    time.sleep(1)
    checkExperience()
    time.sleep(1)
    #Answer all tasks
    try:
        answerMultipleChoice()
        time.sleep(1)
        visaCheck()
        time.sleep(1)
        answerSelect()
        time.sleep(1)
        languageProficiency()
        time.sleep(1)
    except:
        print("nextButton() - Error answering questions")
    
    #Check if next button is review application button
    reviewApp = browser.find_elements(By.XPATH,"//button[@aria-label='Review your application']")
    #If it is review button, begin to click submit
    if len(reviewApp)> 0:
        reviewApp[0].click()
        time.sleep(2)
        submitApplication()
        print("Application submitted")
        return True
    
    try:    
        browser.find_element(By.XPATH,"//button[@aria-label='Continue to next step']").click()
    except:
        print("Next button not found")
        
    return False
    
#Check if application asks if you need visa. Answer No
def visaCheck():
    visaExist = browser.find_elements(By.XPATH,"//span[(contains(., 'visa') or contains(., 'Visa'))]")
    
    if len(visaExist) == 0:
        print('No Visa check')
        return
    else:
        print("Checking visa")
    
    try:
        legend = visaExist[0].find_element(By.XPATH,"./..")
        print(legend.tag_name)
        fieldset = legend.find_element(By.XPATH,"./..")
        print(fieldset.tag_name)
        div = fieldset.find_element(By.XPATH,"//div[@class='fb-radio-buttons']")
        print(div.tag_name)
        buttons = div.find_elements(By.XPATH,"//div[@class='fb-radio display-flex']")
        print(len(buttons))
        noB = buttons[1]
        print(noB.tag_name)
        noInput = noB.find_element(By.XPATH,"//input[@value='No']")
        actions.click(noInput)
        actions.perform()
    except:
        traceback.print_exception()
    
#Exit the job application (Used when application is not supported)
def exitApplication():
    try:
        browser.find_element(By.XPATH,"//li-icon[@class='artdeco-button__icon' and @type='cancel-icon']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//span[contains(., 'Discard')]").click() 
    except:
        print("Cancel button not found")

#If questions asks for years + experience, type 1 in text field
def checkExperience():
    experienceQs = browser.find_elements(By.XPATH,"//span[((contains(., 'experience') or contains(., 'Experience')) or contains(., 'years')) and contains(@class, 't-14')]")
    for question in experienceQs:
        question.click()
        time.sleep(1)
        for i in range(3):
            actions.send_keys(Keys.BACKSPACE)
        actions.perform()
        actions.send_keys('1')
        actions.perform()
        time.sleep(1)

#Answer drop down menu with native english speaking
def languageProficiency():
    dropDown = browser.find_element(By.XPATH,"//span[contains(., 'English') and contains(@class, 't-14')]")
    dropDown.click()
    time.sleep(1)
    actions.send_keys("native")
    actions.perform()
    time.sleep(1)

#Answer all multiple choice quesitons with Yes
def answerMultipleChoice():
    yesAnswer = browser.find_elements(By.XPATH,"//input[contains(@id, 'radio-urn') and contains(@value, 'Yes')]")
    for elements in yesAnswer:
        actions.click(elements)
        actions.perform()
    time.sleep(1)

def answerSelect():
    dropDown = browser.find_elements(By.XPATH,"//select[@class='  fb-dropdown__select']")
    for items in dropDown:
        items.click()
        time.sleep(1)
        actions.send_keys("yes")
        actions.perform()
    time.sleep(1)

#Click submit button
def submitApplication():
    #Scroll down to ensure visibility of button
    for i in range(8):
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH,"//button[@aria-label='Submit application']")))
    submitButton = browser.find_elements(By.XPATH,"//button[@aria-label='Submit application']")
    if len(submitButton) > 0:
        print("submitting")
        time.sleep(5)
        #submitButton[0].click() #commented out so application is not sent for test run
        #time.sleep(2)
        #browser.find_element(By.XPATH,"//li-icon[@type='cancel-icon' and @class='artdeco-button__icon']").click()
        return True
    print(f"Submit button length is: {len(submitButton)}")
    return False
    

def main():
    #Open linkedin.com
    browser.get('http://www.linkedin.com')
    login()
    #time.sleep(15) #Remove if no captcha
    filterJobs()
    time.sleep(2)
    
    #List of jobs
    listings = browser.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
    #Iterate through each job
    x= 0 #Number of listings to go through
    
    #Go through 50 listings
    while(x < 50):
        for listing in listings:
            try:
                listing.click()
                applyToJob()
            except:
                traceback.print_exc()
            time.sleep(2)
        #Update url to load new job listings
        x += 10
        browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3360953405&geoId=103644278&keywords=software%20engineer&location=United%20States&refresh=true&start="+str(x))
        time.sleep(4)
        listings = browser.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
    
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    main()
    