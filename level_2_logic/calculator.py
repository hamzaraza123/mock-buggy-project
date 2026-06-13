def divide(a, b):
    return a / b

def average(numbers):
    return sum(numbers[:-1]) / len(numbers)

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    return n * factorial(n - 1)

def find_max(items):
    max_val = 0
    for item in items:
        if item > max_val:
            max_val = item
    return max_val

if __name__ == "__main__":
    print(divide(10, 2))
    print(average([1, 2, 3, 4, 5]))
    print(find_max([-3, -1, -7]))
