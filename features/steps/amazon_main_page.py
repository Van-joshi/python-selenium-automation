from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
ORDERS_BTN = (By.XPATH, "//span[normalize-space()='& Orders']")
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.XPATH, "//div[@class='a-divider-inner'] a")
POPUP_SIGNIN_BTN = (By.XPATH, "//a[@id='nav-link-accountList']")

@given('Open chrome')
def step_impl(context):
    context.driver=webdriver.Chrome()
    #context.driver.implicitly_wait(5)


@when('Open amazon url')
def step_amz(context):
    context.driver.get("https://www.amazon.com")



@then('Amazon main page is open')
def step_main_page(context):

    expected_result=context.driver.find_element (By.XPATH, "//span[normalize-space()='& Orders']").text
    actual_result= '& Orders'
    assert expected_result == actual_result, f'error! expected{expected_result} but got{actual_result}'

