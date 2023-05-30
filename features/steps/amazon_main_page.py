from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ORDERS_BTN = (By.XPATH, "//span[normalize-space()='& Orders']")
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.XPATH, "//div[@class='a-divider-inner'] a")
POPUP_SIGNIN_BTN = (By.XPATH, "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']")

@given('Open chrome')
def step_impl(context):
    context.driver=webdriver.Chrome()
    #context.driver.implicitly_wait(5)


@when('Open amazon url')
def step_amz(context):
    context.driver.get("https://www.amazon.com")



@when('Amazon main page is open')
def step_main_page(context):

    expected_result=context.driver.find_element (By.XPATH, "//span[normalize-space()='& Orders']").text
    actual_result= '& Orders'
    assert expected_result == actual_result, f'error! expected{expected_result} but got{actual_result}'

@when('Click on Hello Sign In from popup')
def Hello_signin(context):
 context.driver.find_element(By.ID, "nav-link-accountList").click()
 # wait = WebDriverWait(context.driver, 5)
 # context.driver.wait.until(EC.element_to_be_clickable(POPUP_SIGNIN_BTN),message='sign in not visible').click()




 @then('Sign Inn header is visible')
 def Sign_in(context):
    #context.driver.wait.until(EC.url_contains("https://www.amazon.com/ap/signin"))
    expected_result = context.driver.find_element(By.XPATH, "(//h1[@class='a-spacing-small'])").text
    actual_result = 'Sign in'
    assert expected_result == actual_result, f'error! expected{expected_result} but got actual{actual_result}'
