# given lists
first_list = [1, 2, 3, 4, 5]
second_list = [3, 2, 1]


# first division method
import math


def method_one(num_list):
    # first get the product of all items in the list
    product = math.prod(num_list)
    # there are different methods to multiply list items together
    # references: https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
    # https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
    # divide each element at it's position
    return [int(product / num) for num in num_list]
    
    
method_one(first_list)
method_one(second_list)


# without division
def method_two(num_list):
    # at each step find the product of other elements excluding the current element
    return [math.prod(num_list[:index] + num_list[index+1:]) for index in range(0, len(num_list))]
    # there are different filtering methods; for me the above one is easy
    # for reference: https://stackoverflow.com/questions/19286657/index-all-except-one-item-in-python


method_two(first_list)
method_two(second_list)