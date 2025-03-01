import logging

# Configure logging (if not already configured)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_maximum(numbers):
    logging.debug(f"Finding maximum in: {numbers}")
    if not numbers:
        return None
    maximum = max(numbers) # Fixed the bug here
    logging.debug(f"Maximum is: {maximum}")
    return maximum