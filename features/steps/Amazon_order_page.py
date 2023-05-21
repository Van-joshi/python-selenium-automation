from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon main page')
def open_Amazon(context):
    context.driver.get("https://www.amazon.com/")
@ when("Click on orders")
def click_order(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='& Orders']").click()



@then ('Sign In header is visible')
def sign_in_header(context):
     expected_result=context.driver.find_element(By.XPATH, "(//h1[@class='a-spacing-small'])").text
     actual_result= 'Sign in'
     assert expected_result == actual_result, f'error! expected{expected_result} but got actual{actual_result}'


@then('email input field is present')
def email_field(context):
      expected_result1=context.driver.find_element(By.XPATH, "//label[@for='ap_email']").text
      actual_result1= 'Email or mobile phone number'
      assert expected_result1 == actual_result1, f'error! expected{expected_result1} but got actual{actual_result1}'
