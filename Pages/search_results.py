from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class SearchResults(Page):
    Order_Result = (By.XPATH, "(//h1[@class='a-spacing-small'])")
    BOOK_SUBMENU = (By.CSS_SELECTOR, "[data-category='books']")
    BABY_SUBMENU = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SUBMIT_BTN = (By.ID, 'nav-search-submit-button')
    NURSERY = (By.XPATH, "//span[normalize-space()='Nursery']")
    ALL_NURSERY = (By.XPATH, "//h3[normalize-space()='All Nursery']")

    def verify_dpt(self):
     self.wait_for_element_appear(*self.BOOK_SUBMENU)


    def search_for_faust(self):
      return self.driver.find_element(*self.SEARCH_BOX).send_keys('faust')

    def click_on_search_btn(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    #def select_dpt_baby(self):
        #self.wait_for_element_appear(*self.BABY_SUBMENU)

    def search_baby_swing(self):
        return self.driver.find_element(*self.SEARCH_BOX).send_keys('baby swing')


    def verify_dpt_baby(self):
       self.wait_for_element_appear(*self.BABY_SUBMENU)


    def hover_over_nursery(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.NURSERY))
        actions.perform()

    def all_nursery_items_are_seen(self):
        self.wait_for_element_appear(*self.ALL_NURSERY)