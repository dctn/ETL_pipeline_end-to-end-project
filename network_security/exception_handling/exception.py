import sys
from network_security.logging import logger

class SecurityException(Exception):
    def __init__(self,error_msg,error_details:sys):
        self.error_msg = error_msg
        _,_,self.exc_tb = error_details.exc_info()

        self.line_no = self.exc_tb.tb_lineno
        self.file_name = self.exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"\n Error occur in python script: [{self.file_name}] at line: {self.exc_tb.tb_lineno} with error: {self.error_msg}"



if __name__ == '__main__':
    try:
        logger.logging.info("entered try block")
        a = 1/0
    except Exception as e:
        logger.logging.info("entered try except")

        raise SecurityException(e,sys)
