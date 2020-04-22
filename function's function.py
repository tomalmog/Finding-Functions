def find_function(num, func):
    current = 0
    current_test = num
    while True:
        if func(current) == num:
            return current
        elif func(current) > num:
            current_test = current_test / 2
            current -= current_test
        else:
            current_test = current_test / 2
            current += current_test
