from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open amazon main pagee')
def open_Amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Click on Best Sellers')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@when('Hover over language options')
def hover_over_lang(context):
    context.app.header.hover_over_lang()



@then('Amazon Best Sellers text is visible')
def step_best_seller(context):
    expected_result= context.driver.find_element(By.XPATH, "//span[@id='zg_banner_text']").text
    actual_result= 'Amazon Best Sellers'
    assert expected_result == actual_result, f' error! expected{expected_result} but got actual{actual_result}'


@then('New Releases text are seen')
def step_new_release(context):
    expected_result1= context.driver.find_element(By.XPATH, "(//a[@href='/gp/new-releases/ref=zg_bs_tab'])[1]").text
    actual_result1 = 'New Releases'
    assert expected_result1 == actual_result1, f' expected{expected_result1} but got actaul{actual_result1}'


@then('Movers & Shakers text are seen')
def step_M_S(context):
    expected_result2 = context.driver.find_element(By.XPATH, "//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']").text
    actual_result2= 'Movers & Shakers'
    assert expected_result2 == actual_result2, f' expected{expected_result2} but got actual{actual_result2}'


@then('Most Wished For texts are seen')
def step_Most_wished(context):
    expected_result3= context.driver.find_element(By.XPATH, "//a[normalize-space()='Most Wished For']").text
    actual_result3= 'Most Wished For'
    assert expected_result3 == actual_result3, f' expected{expected_result3} but got actual{actual_result3}'


@then('Gift Ideas text are seen')
def step_Gift_ideas(context):
   expected_result4 = context.driver.find_element(By.XPATH, "//a[normalize-space()='Gift Ideas']").text
   actual_result4 = 'Gift Ideas'
   assert expected_result4 == actual_result4, f' expected{expected_result4} but got actual{actual_result4}'


@then('Verify Spanish option is present')
def verify_spanish_is_present(context):
    context.app.header.verify_spanish_is_present()




