# given lists
first_list = [3, 4, -1, 1]
second_list = [1, 2, 0]


def find_lowest_positive(num_list:list):
    # hopping the max runs in linear time
    max_num = max(num_list)
    for itr in range(1, max_num + 2):
        if itr not in num_list:
            return itr
        
# reference: https://stackoverflow.com/questions/41071290/find-the-first-missing-positive-integer-in-python
# reference: https://cs.stackexchange.com/questions/136481/time-complexity-of-min-and-max-on-a-list-of-constant-size
    

find_lowest_positive(second_list)
