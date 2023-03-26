testing_lists = [
    [2, 4, 6, 2, 5],
    [5, 1, 1, 5],
    [0, 1, -1],
    [-10, -5, -12, -1, -7],
    [-7, -10, -12, -2, -16],
    [3, 5, 7, 3, 6]
]


def find_current_largest(num_list: list, index: int) -> int:
    length = len(num_list)
    
    if index >= length:
        return 0
    
    current_max = current_sum = num_list[index]
    for itr in range(index + 2, length + 1):
        current_sum += find_current_largest(num_list, itr)
        if current_sum > current_max:
            current_max = current_sum
            
        current_sum = num_list[index]
        
    return current_max
    

def find_largest_sum(num_list: list) -> int:
    length = len(num_list)
    
    if not length:
        return 0
    if length <= 2:
        return max(num_list)
    
    previous_max = current_max = num_list[0]
    
    for index in range(length):
        current_max = find_current_largest(num_list, index)
        if current_max > previous_max:
            previous_max = current_max
    
    return previous_max
    
    
find_largest_sum(testing_lists[1])
find_largest_sum(testing_lists[2])
find_largest_sum(testing_lists[3])
find_largest_sum(testing_lists[4])
find_largest_sum(testing_lists[5])

# for a simple positive integers, this algorithm is best: https://www.tutorialspoint.com/program-to-find-largest-sum-of-non-adjacent-elements-of-a-list-in-python