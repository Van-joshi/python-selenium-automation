from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

color_options=(By.XPATH, "//div[@id='variation_color_name li']")
current_color1=(By.CSS_SELECTOR, "#variation_color_name .selection")
SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
SUBMIT_BTN = (By.ID, 'nav-search-submit-button')
@given('Amazon main page is open')
def Amazon_main_page(context):
    context.driver.get("https://www.amazon.com")


@when ('Dress is searched on Amazon')
def search_dress(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('dresses')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('User clicks on the dress')
def Select_dress(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Women's Short-Sleeve Scoop Neck Swing Dress").click()
sleep(4)


@then ('All color options are displayed')
def pick_color(context):
    expected_colors=['Black', 'Navy', 'Black, dots', 'Navy/Red, Tossed Leaf/Tulips']
    actual_colors=['Black', 'Navy', 'Black, dots', 'Navy/Red, Tossed Leaf/Tulips']
    colors=context.driver.find_elements(*color_options)
    for color in colors[:4]:
        color.click()
        sleep(4)
        current_color=context.driver.find_element(*current_color1).text
        actual_colors+= current_color
        #assert actual_colors == expected_colors, f' expected{expected_colors} but got{actual_colors}'

