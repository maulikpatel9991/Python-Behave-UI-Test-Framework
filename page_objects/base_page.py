from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from utils.logger import BaseLogging
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = BaseLogging()

    # Open a specific URL
    def open_url(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Opened URL: {url}")
        except Exception as e:
            self.logger.error(f"❌ Error opening URL '{url}': {str(e)}")

    def find_element(self, by, value, timeout=10):
        """Find and return a single element."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))  # ✅ This returns a SINGLE element
            )
            self.logger.info(f"✅ Found element: {element}")  # Debugging log
            return element
        except Exception as e:
            self.logger.error(f"❌ Error finding element {value}: {str(e)}")
            return None  # Return None instead of a list


    # Open a new tab
    def open_new_tab(self, url="about:blank"):
        try:
            self.driver.execute_script(f"window.open('{url}', '_blank');")
            self.logger.info(f"Opened new tab with URL: {url}")
        except Exception as e:
            self.logger.error(f"❌ Error opening new tab: {str(e)}")

    # Get the current URL
    def current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            self.logger.error(f"❌ Error getting current URL: {str(e)}")
            return None

    # Maximize the browser window
    def maximize_window(self):
        try:
            self.driver.maximize_window()
            self.logger.info("Maximized browser window")
        except Exception as e:
            self.logger.error(f"❌ Error maximizing window: {str(e)}")

    # Refresh the current page
    def refresh_page(self):
        try:
            self.driver.refresh()
            self.logger.info("Page refreshed successfully")
        except Exception as e:
            self.logger.error(f"❌ Error refreshing page: {str(e)}")

    # Navigate back in history
    def back_page(self):
        try:
            self.driver.back()
            self.logger.info("Navigated back successfully")
        except Exception as e:
            self.logger.error(f"❌ Error navigating back: {str(e)}")

    # Navigate forward in history
    def forward_page(self):
        try:
            self.driver.forward()
            self.logger.info("Navigated forward successfully")
        except Exception as e:
            self.logger.error(f"❌ Error navigating forward: {str(e)}")

    # Ensure the page has fully loaded
    def get_page_to_load(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            self.logger.info("Page loaded successfully")
        except Exception as e:
            self.logger.error(f"❌ Error waiting for page to load: {str(e)}")

    # Get the current window handle
    def current_window(self):
        try:
            return self.driver.current_window_handle
        except Exception as e:
            self.logger.error(f"❌ Error getting current window handle: {str(e)}")
            return None

    # Switch to a different browser tab by index
    def switch_to_tab(self, index):
        try:
            window_handles = self.driver.window_handles
            if index < len(window_handles):
                self.driver.switch_to.window(window_handles[index])
                self.logger.info(f"Switched to tab {index}")
            else:
                self.logger.error(f"❌ Tab index {index} out of range")
        except Exception as e:
            self.logger.error(f"❌ Error switching to tab {index}: {str(e)}")

    # Close the current tab
    def close_tab(self):
        try:
            self.driver.close()
            self.logger.error("Closed current tab")
        except Exception as e:
            self.logger.error(f"❌ Error closing tab: {str(e)}")

    # Close all tabs and quit the browser
    def close_all_tabs(self):
        try:
            self.driver.quit()
            self.logger.info("Closed all tabs and quit browser")
        except Exception as e:
            self.logger.error(f"❌ Error closing all tabs: {str(e)}")

    # Close all tabs except the first one
    def close_all_tabs_but_one(self):
        try:
            window_handles = self.driver.window_handles
            for handle in window_handles[1:]:
                self.driver.switch_to.window(handle)
                self.driver.close()
            self.driver.switch_to.window(window_handles[0])
            self.logger.info("Closed all tabs except the first one")
        except Exception as e:
            self.logger.error(f"❌ Error closing all tabs but one: {str(e)}")

    # Generate a random string of given length
    def generate_random_string_data(self, length=10):
        try:
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            self.logger.info(f"Generated random string: {random_string}")
            return random_string
        except Exception as e:
            self.logger.error(f"❌ Error generating random string: {str(e)}")
            return None

    # Find multiple elements by selector
    

    # Find a single element by selector
    def find_by(self, by, value, timeout=10):
        try:
            return self.find_element(by, value, timeout)
        except Exception as e:
            self.logger.error(f"❌ Error finding element by {by}: {str(e)}")
            return None

    # Find an element by XPath
    def find_by_xpath(self, xpath, timeout=10):
        try:
            return self.find_element(By.XPATH, xpath, timeout)
        except Exception as e:
            self.logger.error(f"❌ Error finding element by XPath {xpath}: {str(e)}")
            return None

    # Check if an element is selected (for checkboxes, radio buttons, etc.)
    def is_selected(self, by, value):
        try:
            return self.find_element(by, value).is_selected()
        except Exception as e:
            self.logger.error(f"❌ Error checking if element is selected: {str(e)}")
            return False

    # Click an element
    def click_element(self, by, value):
        try:
            element = self.find_element(by, value)
            element.click()
            self.logger.info(f"Clicked element {value}")
        except Exception as e:
            self.logger.error(f"❌ Error clicking element {value}: {str(e)}")

    # Input text into an element
    def enter_text(self, by, value, text):
        try:
            element = self.find_element(by, value)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' into element {value}")
        except Exception as e:
            self.logger.error(f"❌ Error entering text in element {value}: {str(e)}")

    # Check if an element is visible
    def is_element_visible(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False

    # Get the text of an element
    def get_element_text(self, by, value, timeout=10):
        """Get text from a single element."""
        try:
            element = self.find_element(by, value, timeout)  # Get single element
            
            if element:
                self.logger.error(f"✅ Element found: {element.text}")  # Debugging log
                return element.text
            else:
                self.logger.error(f"❌ Element {value} not found")
                return "Element not found"
        except Exception as e:
            self.logger.error(f"❌ Error getting text from element {value}: {str(e)}")
            return ""



    # Scroll to an element
    def scroll_to_element(self, by, value):
        try:
            element = self.find_element(by, value)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Scrolled to element {value}")
        except Exception as e:
            self.logger.error(f"❌ Error scrolling to element {value}: {str(e)}")

    # Take a screenshot
    def take_screenshot(self, filename="screenshot.png"):
        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"Screenshot saved as {filename}")
        except Exception as e:
            self.logger.error(f"❌ Error taking screenshot: {str(e)}")



    def scroll_into_view(self, by, value):
        try:
            element = self.find_element(by, value)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.logger.info(f"Scrolled to element {value}")
        except Exception as e:
            self.logger.error(f"❌ Error scrolling to element {value}: {str(e)}")

    # ===================== Keyboard Actions =====================

    def press_key(self, element, key):
        try:
            element.send_keys(key)
            self.logger.info(f"Pressed key {key}")
        except Exception as e:
            self.logger.error(f"❌ Error pressing key {key}: {str(e)}")

    def press_key_down(self, element):
        self.press_key(element, Keys.ARROW_DOWN)

    def press_key_up(self, element):
        self.press_key(element, Keys.ARROW_UP)

    def press_key_page_down(self, element):
        self.press_key(element, Keys.PAGE_DOWN)

    def press_key_page_up(self, element):
        self.press_key(element, Keys.PAGE_UP)

    def press_key_home(self, element):
        self.press_key(element, Keys.HOME)

    def press_key_end(self, element):
        self.press_key(element, Keys.END)

    def press_key_tab(self, element):
        self.press_key(element, Keys.TAB)

    def press_key_space(self, element):
        self.press_key(element, Keys.SPACE)

    def press_key_enter(self, element):
        self.press_key(element, Keys.ENTER)

    # ===================== Alert Handling =====================

    def accept_alert(self):
        try:
            self.wait.until(EC.alert_is_present()).accept()
            self.logger.info("Accepted alert")
        except Exception as e:
            self.logger.error(f"❌ Error accepting alert: {str(e)}")

    def cancel_alert(self):
        try:
            self.wait.until(EC.alert_is_present()).dismiss()
            self.logger.info("Dismissed alert")
        except Exception as e:
            self.logger.error(f"❌ Error dismissing alert: {str(e)}")

    # ===================== Clipboard & Input Actions =====================

    def paste_keys(self, element):
        self.press_key(element, Keys.CONTROL + "v")

    # ===================== Mouse Actions =====================

    def perform_double_click_action(self, by, value):
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).double_click(element).perform()
            self.logger.info(f"Performed double-click on {value}")
        except Exception as e:
            self.logger.error(f"❌ Error performing double-click: {str(e)}")

    def perform_context_click_action(self, by, value):
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).context_click(element).perform()
            self.logger.info(f"Performed right-click on {value}")
        except Exception as e:
            self.logger.error(f"❌ Error performing right-click: {str(e)}")

    def perform_click_and_hold_action(self, by, value):
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).click_and_hold(element).perform()
            self.logger.info(f"Performed click-and-hold on {value}")
        except Exception as e:
            self.logger.error(f"❌ Error performing click-and-hold: {str(e)}")

    def perform_click_action_with_offset(self, by, value, x_offset, y_offset):
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).move_to_element_with_offset(element, x_offset, y_offset).click().perform()
            self.logger.info(f"Performed click at offset ({x_offset}, {y_offset}) on {value}")
        except Exception as e:
            self.logger.error(f"❌ Error performing click with offset: {str(e)}")

    def perform_move_to_element(self, by, value):
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info(f"Moved to element {value}")
        except Exception as e:
            self.logger.error(f"❌ Error moving to element {value}: {str(e)}")

    def perform_drag_and_drop_action(self, source_by, source_value, target_by, target_value):
        try:
            source = self.find_element(source_by, source_value)
            target = self.find_element(target_by, target_value)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            self.logger.info(f"Performed drag and drop from {source_value} to {target_value}")
        except Exception as e:
            self.logger.error(f"❌ Error performing drag-and-drop: {str(e)}")

    # ===================== Dropdown Handling =====================

    def select_dropdown_item(self, by, value, item_text):
        from selenium.webdriver.support.ui import Select
        try:
            element = self.find_element(by, value)
            select = Select(element)
            select.select_by_visible_text(item_text)
            self.logger.info(f"Selected '{item_text}' from dropdown {value}")
        except Exception as e:
            self.logger.error(f"❌ Error selecting from dropdown {value}: {str(e)}")

    # ===================== File Upload =====================

    def upload_with_drag_and_drop(self, file_path, by, value):
        try:
            element = self.find_element(by, value)
            element.send_keys(file_path)
            self.logger.info(f"Uploaded file {file_path}")
        except Exception as e:
            self.logger.error(f"❌ Error uploading file {file_path}: {str(e)}")