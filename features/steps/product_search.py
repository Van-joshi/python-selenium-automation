from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.Amazon.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shoes')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
sleep(1)


@then('Product results for shoes are shown')
def verify_found_results_text(context):
    all_products=context.driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
    #print(all_products)
    for product in all_products:
        title=product.find_element(By.XPATH, "(//span[@class='a-size-base-plus a-color-base'][normalize-space()='Amazon Essentials'])[1]").text
        print(title)





