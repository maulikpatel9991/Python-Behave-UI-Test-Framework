from behave import given, then
from page_objects.home_page import HomePage

# Step Definition: Open the Website
@given("I open the website")
def step_impl(context):
    """Opens the website using the HomePage object."""
    context.home_page = HomePage(context.driver)  # Initialize HomePage object
    context.home_page.open_url(context.base_url)   # Open the website URL

# Step Definition: Verify the Logo is Visible
@then("I should see the logo")
def step_impl(context):
    """Checks if the website logo is visible on the homepage."""
    context.home_page = HomePage(context.driver)  # Ensure HomePage is initialized
    assert context.home_page.is_logo_visible(), "❌ Logo is not visible!"
