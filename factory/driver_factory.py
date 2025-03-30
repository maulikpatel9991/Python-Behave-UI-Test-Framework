# from selenium import webdriver

# class DriverFactory:
#     @staticmethod
#     def create_driver(browser="chrome"):
#         if browser == "chrome":
#             options = webdriver.ChromeOptions()
#             options.add_argument("--headless")
#             return webdriver.Chrome(options=options)
#         elif browser == "firefox":
#             options = webdriver.FirefoxOptions()
#             options.add_argument("--headless")
#             return webdriver.Firefox(options=options)
#         else:
#             raise ValueError(f"Unsupported browser: {browser}")
