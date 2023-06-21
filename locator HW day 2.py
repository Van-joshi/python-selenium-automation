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
# Amazon logo
driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
# Email Field
# driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()
# driver.find_element(By.ID, "ap_email").send_keys("vjtest@gmail.com")
# driver.find_element(By.ID, "continue").click()
# driver.find_element(By.XPATH, "(//span[@class='a-expander-prompt'])[1]")
# driver.find_element(By.ID, "ap-other-signin-issues-link")
# driver.find_element(By.ID, "createAccountSubmit")
#driver.find_element(By.XPATH, "//a[@class='a-link-normal'][normalize-space()='Conditions of Use']")
#driver.find_element(By.XPATH, "//a[@class='a-link-normal'][normalize-space()='Privacy Notice']")
driver.find_element(By.XPATH, "//span[normalize-space()='& Orders']").click()
expected_result= 'Mobile phone number or email'
actual_result=driver.find_element(By.XPATH, "//label[normalize-space()='Mobile phone number or email']").text
if expected_result == actual_result:
    print("Test Passed")
expected_result1= 'Sign in'
actual_result1=driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']").text
#if expected_result1 == actual_result1:
assert expected_result1==actual_result1, f'Expected{expected_result1} but got{actual_result1}'
  # print("Test 1 passed")