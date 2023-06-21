from Pages.base_page import Page
from selenium.webdriver.common.by import By


class CartStatus(Page):
    Cart_Status = (By.CLASS_NAME, "nav-cart-icon nav-sprite")
    EMPT_SHOP_CART = (By.CSS_SELECTOR, "div[class='a-row sc-your-amazon-cart-is-empty'] h2")

    def shopping_cart(self):
        #self.verify_element_text(*self.Cart_Status)
        self.driver.find_element(*self.Cart_Status).click()

    def empty_cart_text(self):
            # actual_text = self.driver.find_element(*EMPT_SHOP_CART).text
            # assert expected_text == actual_text, \
            #     f'Checking by locator {EMPT_SHOP_CART}. Expected {expected_text}, but got {actual_text}'
            self.verify_element_text('Your Amazon Cart is empty',*self.EMPT_SHOP_CART)

        #expected_result1= 'Your Amazon Cart is empty'
        #actual_result1= self.driver.find_element(self.Cart_Status).text
        #assert expected_result1 == actual_result1, f' error! expected{expected_result1} but got actual{actual_result1}'
