from Pages.base_page import Page
from selenium.webdriver.common.by import By


class OrdersPage(Page):
    EMPT_SHOP_CART = (By.ID,"div[class='a-row sc-your-amazon-cart-is-empty'] h2")


def empty_shop_cart(self):
    self.find_element(*self.EMPT_SHOP_CART).text()