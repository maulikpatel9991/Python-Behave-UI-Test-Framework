from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from locators import page_locator as locator

class HomePage(BasePage):
    """
    Page Object Model (POM) for the Home Page.
    - Inherits from BasePage.
    - Contains methods to interact with home page elements.
    """

    def __init__(self, driver):
        """
        Constructor to initialize the HomePage object.
        
        :param driver: WebDriver instance used for automation.
        """
        super().__init__(driver)

    def is_logo_visible(self):
        """
        Checks if the homepage logo is visible.
        
        :return: True if the logo is found, otherwise False.
        """
        return len(self.driver.find_elements(*locator.HomePage.LOGO_LOCATOR)) > 0
