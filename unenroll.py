#add your Credentials, Number of courses you want to delete and Selenium Chrome Driver path here
emailId = "Enter your email id here"
password = "Enter your password here"
nCourses = 5
driverPath = 'Path to your selenium chrome driver'

#importing libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#set configuration
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path = driverPath , options = options)


#FUNCTION DEFINITIONS

#funtion to login using above defined credentials on coursera login page
def login():
    driver.find_element(By.ID,'email').send_keys(emailId)
    time.sleep(1)
    driver.find_element(By.ID,'password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[@class="_6dgzsvq css-1af0gyj"]').click()

#funtion to click unenroll button as it is stale in default state
def find(driver):
    element = driver.find_element(By.XPATH,'//li[@data-e2e="dropdown-option-uneroll"]')
    if element:
        return element
    else:
        return False

#funtion to actually click unenroll and follow through
def unEnroll():
    driver.find_element(By.XPATH,'//button[@class="meatball-menu-button"]').click()
    time.sleep(1)
    unenroll_button = WebDriverWait(driver, 5).until(find)
    unenroll_button.click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//button[@data-e2e="unenroll-button-logged-in-home"]').click()

#funtion to remove close promotional dialog box (can delete this part if popup not present)
def removePopup():
    for i in range(2):
        try:
            driver.find_element(By.XPATH,'//button[@data-track-component="dismiss_action"]').click()
        except:
            pass

#DRIVER CODE

#visit login page
driver.get('https://www.coursera.org/?authMode=login')

#login
login()

#default sleep time is 10 sec because of captcha intervention(solve manually if popup)
time.sleep(10)

#visit enrolled courses page
driver.get('https://www.coursera.org/in-progress')

time.sleep(3)

#scroll down for proper execution
driver.execute_script("window.scrollTo(0, 300)")

time.sleep(3)

removePopup()

time.sleep(2)

for i in range(nCourses):
    unEnroll()
    time.sleep(10)