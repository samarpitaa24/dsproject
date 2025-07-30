import sys
from src.dsproject.logger import logging

import sys
import traceback

def error_message_detail(error, error_detail: sys):
    """ GENERIC CODE
    Returns a detailed error message with file name and line number where the error occurred.

    Parameters:
    -----------
    error : Exception
        The actual exception object raised.
    error_detail : sys
        The sys module passed to extract traceback information (usually just pass `sys`).

    Returns:
    --------
    str
        A formatted string describing the error with filename, line number, and the error message.
    """
    # Get exception traceback object
    _, _, exc_tb = error_detail.exc_info() #returns 3 info out of which we use only exc_tb

    # Extract file name and line number from traceback
    file_name = exc_tb.tb_frame.f_code.co_filename #from exc_tb we're getting required info abt file, filename is where exception occurs
    
    # Properly format the error message
    error_message = f"Error occurred in python script name [{0}], line number [{1}], error message:[ {2}]".format(file_name, exc_tb.tb_lineno,str(error))

    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_details: sys): #sys will tell details of error
        super().__init__(error_message) #since customexception is inheriting exception hence super
        self.error_message = error_message_detail(error_message, error_details)
        
    def __Str__(self):
        return self.error_message