from utils import find_maximum, find_minimum

def main():
    numbers = [1, 2, 3, 10] 
    max_number = find_maximum(numbers)
    min_number = find_minimum(numbers)
    print(f"Maximum number is: {max_number}")
    print(f"Minimum number is: {min_number}")

if __name__ == "__main__":
    main()