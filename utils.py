def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)  # Bug: Should use max(numbers) instead of max(numbers[:-1])
