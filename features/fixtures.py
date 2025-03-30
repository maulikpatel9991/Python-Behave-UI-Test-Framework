from behave import fixture

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
@fixture(name="chrome")
def browser_chrome(context):
    chrome_options = webdriver.ChromeOptions()
    yield chrome_options
    