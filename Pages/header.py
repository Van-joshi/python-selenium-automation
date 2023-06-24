from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, "nav-orders")
    SEARCH_ICON = (By.ID, '"nav-search-submit-button"')
    #HELLO_SIGNIN =(By.ID, 'nav-link-accountList')
    POPUP_SIGNIN_BTN = (By.ID, "nav-signin-tooltip")
    LANG_DROPDOWN = (By.ID, 'icp-nav-flyout')
    SHOPPING_CART = (By.ID, 'nav-cart-text-container')
    SIGNIN_TEXT = (By.XPATH, "(//h1[@class='a-spacing-small'])")
    EMAIL_BOX = (By.ID, 'ap_email')
    LANGUAGE_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    DEPT_SELECT = (By.ID, 'searchDropdownBox')


    def click_on_order(self):
        self.click(*self.ORDERS_BTN)

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def searchbar_field(self, *locator):
        return self.driver.find_element(*self.SEARCH_FILED)

    def sign_in_popup(self):
        self.wait_for_element_click(*self.POPUP_SIGNIN_BTN)

    def Lang_dropdown(self):
        self.find_element(*self.LANG_DROPDOWN)

    def click_shopping_cart(self):
        self.click(*self.SHOPPING_CART)

    def hover_over_lang(self):
        #lang_options = self.find_element(*self.LANGUAGE_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.LANGUAGE_OPTIONS))
        actions.perform()


    def verify_spanish_is_present(self):
     self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self):
        dept_select = (self.find_element(*self.DEPT_SELECT))
        select = Select(dept_select)
        select.select_by_value('search-alias=stripbooks')

    def select_dpt_baby(self):
        dept_select = (self.find_element(*self.DEPT_SELECT))
        select = Select(dept_select)
        select.select_by_value('search-alias=baby-products')

