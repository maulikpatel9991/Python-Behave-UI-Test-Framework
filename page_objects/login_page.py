from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from locators import page_locator as locator

class LoginPage(BasePage):
    """
    Page Object Model (POM) for the Login Page.
    - Inherits from BasePage.
    - Contains methods to interact with login page elements.
    """

    def __init__(self, driver):
        """
        Constructor to initialize the LoginPage object.
        
        :param driver: WebDriver instance used for automation.
        """
        super().__init__(driver)

    def header_text_visible(self):
        """
        Checks if the login page header text (logo) is visible and returns the text.
        
        :return: The header text if found, otherwise an empty string.
        """
        self.is_element_visible(*locator.Login.TEXT_LOCATOR)  # Ensure the element is visible
        header_text = self.get_element_text(*locator.Login.TEXT_LOCATOR)  # Get text from the element
        return header_text
