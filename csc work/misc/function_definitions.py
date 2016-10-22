# double: takes a number and returns twice its value
# double(7) produces 14
# double(5.7) produces 11.4
def double(num):
    return 2 * num

# our_maximum: takes two numbers and returns the larger one
# our maximum(4, 3.7) produces 4
def our_maximum(num1, num2):
    return max(num1, num2)

# max_of_min(4, 3.7, 6, 3.5)
# produces 3.7
# max_of_min(1, 1.7, 4.5, 3)
# produces 3
def max_of_min(num1, num2, value1, value2):
    min1 = min(num1, num2)
    min2 = min(value1, value2)
    return max(min1, min2)
