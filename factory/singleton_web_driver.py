import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverManager:
    _driver = None

    @staticmethod
    def get_driver(browser="chrome", mode='headless'):
        """Initializes the driver dynamically based on command-line input."""
        if WebDriverManager._driver is None:
            options = None

            if browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--headless")
                if mode == "headless":
                    options.add_argument("--headless")

                WebDriverManager._driver = webdriver.Chrome(
                    ChromeDriverManager().install(), options=options
                )

            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
                if mode == "headless":
                    options.add_argument("--headless")

                WebDriverManager._driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install(), options=options
                )

            elif browser == "edge":
                options = webdriver.EdgeOptions()
                if mode == "headless":
                    options.add_argument("--headless")

                WebDriverManager._driver = webdriver.Edge(
                    executable_path=EdgeChromiumDriverManager().install(), options=options
                )

        return WebDriverManager._driver

    @staticmethod
    def quit_driver():
        """Closes the WebDriver instance."""
        if WebDriverManager._driver:
            WebDriverManager._driver.quit()
            WebDriverManager._driver = None

    # @staticmethod
    # def parse_arguments():
    #     parser = argparse.ArgumentParser(description="WebDriver Configuration")

    #     parser.add_argument("--browser", choices=["chrome", "firefox", "edge"], default="chrome",
    #                         help="Choose browser for test execution")
    #     parser.add_argument("--mode", choices=["web", "headless"], default="web",
    #                         help="Choose browser execution mode (default = web)")
        
    #     parser.add_argument("--environment", choices=["staging", "dev", "production"], default="staging",
    #                     help="==> Environment to execute the tests (default = staging). Find the app URLs in properties file")
        
    #     parser.add_argument("--orientation", choices=["Landscape", "Portrait"], default="Portrait",
    #                     help="==> Screen orientation for mobile executions (default = Portrait)")
    
    #     parser.add_argument("--resolution", choices=["1024x768", "1280x1024", "1600x1200", "1920x1080"], default="1280x1024",
    #                         help="==> Resolution for web execution (default = 1280x1024)")
        
    #     parser.add_argument("--tags", default="",
    #                         help="==> Feature(s) / Scenario(s) to be executed (separate tags by comma)")
        
    #     parser.add_argument("--exclude", choices=["wip", "skip", "bug", "slow", "obsolete", ""], default="",
    #                     help="==> Scenarios to be ignored (e.g., wip)")


    #     return parser.parse_args()
