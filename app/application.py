from Pages.header import Header
from Pages.main_page import MainPage
from Pages.search_results import SearchResults
from Pages.cart_status import CartStatus
from Pages.sign_in_page import SignInPage
from Pages.orders_page import OrdersPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results = SearchResults(self.driver)
        self.cart_status = CartStatus(self.driver)
        self.orders_page = OrdersPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)



