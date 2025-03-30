from utils.logger import BaseLogging


class RunningException:
    """
    A utility class for handling and raising custom exceptions with logging.
    """

    @staticmethod
    def raise_assertion_error(custom_message, exception):
        """
        Raises an AssertionError with a custom message and logs the error.

        Parameters:
        - custom_message (str): Custom message to describe the error.
        - exception (Exception): The original exception object.

        Raises:
        - AssertionError: Raised with a formatted error message.
        """
        message = BaseLogging.show_exception("   ", custom_message, exception)
        BaseLogging.error(message)  # Log the error message
        raise AssertionError(message)  # Raise an AssertionError with details

    @staticmethod
    def raise_exception_error(custom_message, exception):
        """
        Raises a generic Exception with a custom message and logs the error.

        Parameters:
        - custom_message (str): Custom message to describe the error.
        - exception (Exception): The original exception object.

        Raises:
        - Exception: Raised with a formatted error message.
        """
        message = BaseLogging.show_exception("EXCEPTION: ", custom_message, exception)
        BaseLogging.error(message)  # Log the error message
        raise Exception(message)  # Raise a generic Exception with details
