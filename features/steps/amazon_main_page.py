from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver

@given('Open chrome')
def step_impl(context):
    context.driver=webdriver.Chrome()

@when('Open amazon url')
def step_amz(context):
    context.driver.get("https://www.amazon.com")


@then('Amazon main page is open')
def step_main_page(context):
    expected_result=context.driver.find_element (By.XPATH, "//span[normalize-space()='& Orders']").text
    actual_result= '& Orders'
    assert expected_result == actual_result, f'error! expected{expected_result} but got{actual_result}'

