#logs = contain information, better version of printing bc it has a purpose
#mostly used for reporting information and its severity of knowledge

import logging

#default, root yung nag log
logging.debug('This is a debug message') #will not be logged

logging.info('This is an info message')
logging.info('you can set the level and message!!, but this will not be logged')

#only warning and above will be logged
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')