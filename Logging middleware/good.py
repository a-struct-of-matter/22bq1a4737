import logging
from functools import wraps
from datetime import datetime


# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_middleware(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"Called {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} succeeded with result={result}")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} failed with error: {e}", exc_info=True)
            raise
    return wrapper

@log_middleware
def example_function(x, y):
    return x / y
