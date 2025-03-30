import logging
import json
import os
from utils.StringsUtil import StringUtil
from utils.TextColorUtil import TextColor as Color

# ==============================================================
# Initialize Logger Configuration
# ==============================================================

logger = logging.getLogger(__name__)  # Create a logger instance
logger.setLevel(logging.ERROR)  # Set logging level to ERROR

# Define Log Directory and Log File
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_execution.log")

# Create 'logs' directory if it does not exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging to write logs to a file
logging.basicConfig(
    filename=LOG_FILE,  # Log file path
    level=logging.DEBUG,  # Logging level
    format="[%(levelname)-2s %(asctime)s]: %(message)s",  # Log message format
    filemode="w",  # Overwrites logs on each run; use "a" to append
)

logger = logging.getLogger(__name__)  # Reinitialize logger


# ==============================================================
# BaseLogging Class: Provides Logging Utility Functions
# ==============================================================
class BaseLogging:
    """
    A utility class for logging messages with different severity levels.
    It also supports color-coded messages and response handling.
    """

    @staticmethod
    def display_debug_error(message):
        """Logs an error message and prints it in red."""
        logger.error(Color.red(f"   ERROR: {message}"), exc_info=True)

    @staticmethod
    def show_response(response, show_header=False):
        """
        Displays HTTP response details.
        
        Parameters:
        - response (Response): The HTTP response object.
        - show_header (bool): If True, displays the response headers.
        """
        try:
            if show_header:
                BaseLogging.info("-- HEADER --")
                print(Color.blue(response.headers) + "\n")

            # Parse and display the response body
            parsed_body = json.loads(str(response.text))
            BaseLogging.info("-- RESPONSE BODY --")
            print(Color.blue(StringUtil.indent_dict_body(parsed_body)))
        except Exception as ex:
            message = BaseLogging.show_exception(
                "EXCEPTION: ", "Unable to retrieve response body! ", ex
            )
            BaseLogging.error(message)
            raise Exception(message)

    @staticmethod
    def status_passed():
        """Prints a green-colored message indicating a test step has passed."""
        print(Color.green("   >>>>>>> STEP PASSED!  <<<<<<<\n"))

    @staticmethod
    def status_failed(stacktrace=""):
        """Prints a red-colored message indicating a test step has failed."""
        print(Color.red(f"   ERROR IN: {stacktrace}"))
        print(Color.red("\n   >>>>>>> STEP FAILED!  <<<<<<<\n"))

    @staticmethod
    def error(message="", display_msg_config=False):
        """
        Logs and prints an error message.

        Parameters:
        - message (str): The error message to be logged.
        - display_msg_config (bool): If True, displays debug error details.
        """
        logger.error(Color.red(f"   ERROR :: {message}"))
        print(Color.red(f"   ERROR :: {message}"))
        if display_msg_config:
            BaseLogging.display_debug_error(message)

    @staticmethod
    def warning(message=""):
        """Prints a yellow-colored warning message."""
        print(Color.yellow(f"   WARN :: {message}"))

    @staticmethod
    def info(message=""):
        """Logs and prints an info message in blue."""
        logger.info(Color.blue(f"   INFO :: {message}"))
        print(Color.blue(f"\n   :: {message}"))

    @staticmethod
    def success(message=""):
        """Logs and prints a success message in green."""
        logger.info(Color.green(f"   SUCCESS :: {message}"))
        print(Color.green(f"   :: (\u2713) {message}"))

    @staticmethod
    def show_exception(title, custom_message, exception):
        """
        Formats and returns an exception message.
        
        Parameters:
        - title (str): The title of the exception.
        - custom_message (str): Custom message describing the exception.
        - exception (Exception): The exception object.

        Returns:
        - str: Formatted exception message.
        """
        message = f"\n{BaseLogging.create_header_with_top_marker(title, custom_message, '', '-')}\n\n(+) Causes:\n{exception}"
        return message
