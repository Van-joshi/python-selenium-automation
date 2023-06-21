from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):
    SIGNIN_TEXT = (By.XPATH, "(//h1[@class='a-spacing-small'])")
    EMAIL_BOX = (By.ID, 'ap_email')
    CONTINUE_BTN = (By.ID, 'continue')
    CREATE_UR_AMZ_ACT = (By.ID, 'createAccountSubmit')

    def sign_in_header(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        self.verify_element_text('Sign in',*self.SIGNIN_TEXT)


    def email_input_field(self):
        self.find_element(*self.EMAIL_BOX)


    def create_amz_act(self):
        self.find_element(*self. CREATE_UR_AMZ_ACT).click()


    def signin_cont_btn(self):
        self.find_element(*self. CONTINUE_BTN).click()
