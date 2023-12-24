# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n == 42:  # checking if value is already 42
        return True
    elif n < 42:  # any number less than 42 is automatically False
        return False
    else:  # checking each condition to consider all operation possibilities, for numbers that meet multiple conditions
        return \
            ((n % 2 == 0) and bears(n // 2)) or \
            ((n % 3 == 0 or n % 4 == 0) and n % 10 * n % 100 and bears(n - n % 10 * n % 100)) or \
            ((n % 5 == 0) and bears(n - 42))