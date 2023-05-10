from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-link-accountList').click()
driver.find_element(By.ID, 'createAccountSubmit').click()
#logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# form
driver.find_element(By.ID, 'ap_customer_name')

driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.CLASS_NAME, 'a-button-input')

# #Conditions of use and Privacy Ntice
driver.find_element(By.XPATH, ("//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]"))
driver.find_element(By.XPATH, ("(//a[contains(text(),'Privacy Notice')])[1]"))
driver.find_element(By.XPATH, "//a[normalize-space()='Sign in']")






