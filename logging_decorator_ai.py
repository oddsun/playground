import logging

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Test the logger
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

def log_decorator(func):
    """
    A decorator that wraps the passed in function and logs.

    Logs start, end, duration, args, kwargs, and result of the function. Uses varying levels of logging based on the content.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log the start of the function
        logger.info('starting')
        logger.debug(f'{args=}, {kwargs=}')

        # Call the function being decorated and capture the result
        result = func(*args, **kwargs)

        # Log the end of the function
        logger.info('completed')

        # Return the result of the decorated function call
        return result

    return wrapper