from utils import configutils as conf
from factory.singleton_web_driver import WebDriverManager
import argparse
import allure
from allure_behave.hooks import allure_report
from utils.logger import BaseLogging
import os


def before_all(context):
    """
    Hook executed before all tests start.
    - Creates the reports directory if it doesn’t exist.
    - Initializes base URLs (API & Web).
    - Sets up the WebDriver instance.
    """
    report_dir = "reports/allure-results"
    
    # Ensure the reports directory exists
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Retrieve API and Web URLs from config
    context.api_url = conf.get_apiurl()
    context.base_url = conf.get_url()
    BaseLogging.info(f"✅ URLs from application are ready! {context.base_url}")

    # Default browser and mode (can be modified dynamically)
    browser = "chrome"
    mode = "web"

    # Store report directory path in context
    context.allure_report_directory = report_dir

    # Initialize WebDriver
    context.driver = WebDriverManager.get_driver(browser, mode)



def after_all(context):
    """
    Hook executed after all tests complete.
    - Closes the WebDriver session.
    """
    WebDriverManager.quit_driver()


def after_scenario(context, scenario):
    """
    Hook executed after each scenario.
    - If a scenario fails, captures a screenshot and attaches it to the Allure report.
    """
    if scenario.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),  # Capture screenshot
            name="screenshot",  # Screenshot name
            attachment_type=allure.attachment_type.PNG  # Image type
        )


# -------------------- Optional Shell Commands --------------------
# These commands allow dynamic execution of tests with parameters.
# Example usage:
# ENVIRONMENT=${1:-staging}
# TARGET=${2:-local}
# BROWSER=${3:-chrome}
# MODE=${4:-web}
# 
# Run tests with:
# behave --environment=$ENVIRONMENT --target=$TARGET --browser=$BROWSER --mode=$MODE
