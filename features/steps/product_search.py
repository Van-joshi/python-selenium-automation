from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
Product_match=(By.XPATH, "(//span[@class='a-size-base-plus a-color-base'][normalize-space()='Amazon Essentials'])[1]")


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


@when('Select department books')
def select_department(context):
    context.app.header.select_department()


@when('Search for faust')
def search_for_faust(context):
    context.app.search_results.search_for_faust()


@when('Select department baby')
def select_dpt_baby(context):
    context.app.header.select_dpt_baby()


@when('Search for baby swing')
def search_baby_swing(context):
    context.app.search_results.search_baby_swing()

@when('Hover over nursery')
def hover_over_nursery(context):
    context.app.search_results.hover_over_nursery()

@then('All nursery items are seen')
def all_items_are_seen(context):
    context.app.search_results.all_nursery_items_are_seen()


@then('Product results for shoes are shown')
def verify_found_results_text(context):
    all_products=context.driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
    #print(all_products)
    for product in all_products:
        title=product.find_element(*Product_match).text
        print("title is:"+ " "+ title)


@then('Verify correct result is shown')
def verify_dpt(context):
    context.app.search_results.verify_dpt()


@then('Verify baby department is shown')
def verify_dpt_baby(context):
    context.app.search_results.verify_dpt_baby()
