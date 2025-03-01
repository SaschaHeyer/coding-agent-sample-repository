import logging
from utils import find_maximum

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    numbers = [1, 2, 3, 10] 
    max_number = find_maximum(numbers)
    logging.info(f"Maximum number is: {max_number}")

if __name__ == "__main__":
    main()
