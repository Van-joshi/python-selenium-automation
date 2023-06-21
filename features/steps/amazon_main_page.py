from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.common.exceptions import TimeoutException


ORDERS_BTN = (By.ID, "nav-orders")
SEARCH_FILED = (By.ID, "twotabsearchtextbox")
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.XPATH, "//div[@class='a-divider-inner'] a")
POPUP_SIGNIN_BTN = (By.ID, "nav-signin-tooltip")
SIGNIN_TEXT = (By.XPATH, "(//h1[@class='a-spacing-small'])")



@given('Open chrome')
def step_impl(context):

    context.driver = webdriver.Chrome()


# context.driver.implicitly_wait(5)
@when('Open amazon url')
def step_amz(context):
    #context.driver.get("https://www.amazon.com")
    context.app.main_page.open_main_page()


#@when('Amazon main page is open')
#def step_main_page(context):
    #expected_result = 'Returns & Orders'
    #context.app.header.click_on_order()
    #actual_result = context.driver.find_element(*ORDERS_BTN).text
    #assert expected_result == actual_result, f'error! expected{expected_result} but got{actual_result}'


@when('Click on Hello Sign In from popup')
def Hello_signin_locator(context):

    # context.driver.wait.until(EC.element_to_be_clickable(POPUP_SIGNIN_BTN)).click()
    context.app.header.sign_in_popup()


@then ('Sign Inn header is visible')
def sign_in_header(context):
    context.app.header.sign_in_header()
    # expected_result = 'Sign in'

    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    # actual_result = context.driver.find_element(*SIGNIN_TEXT).text
    # assert expected_result == actual_result, f'error! expected{expected_result} but got actual{actual_result}'


