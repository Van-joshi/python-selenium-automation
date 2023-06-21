from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

EMAIL_BOX = (By.ID, 'ap_email')
SIGNIN_TEXT = (By.XPATH, "(//h1[@class='a-spacing-small'])")
EMPTY_CART = (By.CSS_SELECTOR, "div[class='a-row sc-your-amazon-cart-is-empty'] h2")


@given('Open amazon main page')
def open_Amazon(context):
    #context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_main_page()


@ when("Click on orders")
def click_order(context):
    #context.driver.find_element(By.XPATH, "//span[normalize-space()='& Orders']").click()
    context.app.header.click_on_order()


@then ('Sign In header is visible')
def sign_in_header(context):

    expected_result = 'Sign in'
    context.app.sign_in_page.sign_in_header()


@then('email input field is present')
def email_input_field(context):
    #context.driver.find_element(*EMAIL_BOX)
    context.app.sign_in_page.email_input_field()


@then('Navigate back to main page')
def navigate_back(context):
    context.driver.back()


@then('click on shopping cart')
def click_on_shopping_cart(context):
    context.app.header.click_shopping_cart()


@then('verify cart is empty')
def verify_cart_is_empty(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/cart'))
    expected_result = 'Your Amazon Cart is empty'
    # actual_result2 = context.driver.find_element(*EMPTY_CART).text
    # assert expected_result2 == actual_result2, f'error! expected{expected_result2} but got actual{actual_result2}'
    context.app.cart_status.empty_cart_text()

