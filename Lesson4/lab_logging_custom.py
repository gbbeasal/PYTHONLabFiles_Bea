###using getLogger let's you log as some entity other than root
import logging

logging.basicConfig(
    filename = 'example3.log',
    level=logging.DEBUG,
)
#logger = logging.getLogger() 
logger = logging.getLogger(__name__) 
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')