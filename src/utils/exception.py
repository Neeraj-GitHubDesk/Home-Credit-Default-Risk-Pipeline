import sys

def get_error_detail(error, error_detail: sys):
    """
    Extract detailed error information including
    filename and line number where exception occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error in '{file_name}', line {line_number}: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Store the formatted error message
        self.error_message = get_error_detail(error_message, error_detail)

    def __str__(self):
        # When printing exception, return detailed error info
        return self.error_message