from behave import given, then
from page_objects.login_page import LoginPage
# Importing necessary utilities for JSON data and logging
from utils.helpers import read_json_data
from utils.logger import BaseLogging

# Step Definition: Navigate to the Automation Exercise Website
@given("I navigate to the Automation Exercise website")
def step_navigate_to_website(context):
    """Opens the Automation Exercise website using the LoginPage object."""
    context.login_page = LoginPage(context.driver)  # Initialize the LoginPage object
    context.login_page.open_url(context.base_url)   # Open the website URL

# Step Definition: Verify Home Page Header Text
@then("I should see the home page header text")
def step_verify_home_page_header(context):
    """Validates that the header text matches expected text from JSON data."""
    context.login_page = LoginPage(context.driver)  # Ensure LoginPage is initialized
    text = context.login_page.header_text_visible()  # Get the header text from the webpage

    # Load expected text from JSON file
    data = read_json_data('factory/test_context_data.json')

    # Validate that the actual text matches the expected positive scenario text
    assert text == data['login_header_text']['positive']['text'], \
        f"Expected '{data['login_header_text']['positive']['text']}', but got '{text}'"
