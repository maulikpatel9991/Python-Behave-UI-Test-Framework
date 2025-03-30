from selenium.webdriver.common.by import By

class Login:
    """
    Locators for the Login Page.
    """
    TEXT_LOCATOR = (By.XPATH, "//div[@class='login_logo']")  # Locator for the login page header/logo


class HomePage:
    """
    Locators for the Home Page.
    """
    LOGO_LOCATOR = (By.XPATH, "//div[@class='login_logo']")  # Locator for the home page logo
