from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median(num):
    try:
        num_values = len(num)
        num.sort()
        if num_values % 2 == 0:
            median1 = num[int(num_values // 2)]
            median2 = num[int(subtraction((num_values // 2), 1))]
            median_result = division(addition(median1, median2), 2)
        else:
            median_result = num[int(division(num_values, 2))]
        return median_result
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")