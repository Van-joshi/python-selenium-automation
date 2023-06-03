from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

privacy_link=(By.XPATH, "//a[@class='a-link-normal'][normalize-space()='Privacy Notice']")
@then ('Store Original window')
def store_original_window(context):
    context.original_window=context.driver.current_window_handle
    print("Original:", context.original_window )
    print("All Windows:", context.driver.window_handles )
@then('Click on Privacy Notice')
def click_on_pn(context):
    context.driver.find_element(*privacy_link).click()
    print("All windows:", context.driver.window_handles)

@then('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows=context.driver.window_handles
    print("After all windows are open-All windows:", all_windows)
    context.driver.switch_to.window(all_windows[1])
@then( 'TC Page is Open')
def tc_page_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display'))

@then('Close TC page')
def close_tc_page(context):
    context.driver.close()

@then('Return to original window')
def return_to_org_window(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.original_window)
    print("original", context.original_window)











