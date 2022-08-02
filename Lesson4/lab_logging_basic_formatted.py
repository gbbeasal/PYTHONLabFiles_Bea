#Logging/Saving logs to a file = use logging.basicConfig():
#if the file you specified doesnt exist, it will be created.
#Else, newer logs will be appended.

import logging
#logging.basicConfig(filename='example.log', level=logging.DEBUG) <-- normie, no format
logging.basicConfig(
    filename = 'example2.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

print(type(logging.debug('This message should go to the log file')))