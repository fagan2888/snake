def max_of_min(num1, num2, value1, value2):
	min_num = min(num1, num2)
	min_val = min(value1, value2)
	return max(min_num, min_val)
