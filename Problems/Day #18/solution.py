def find_each_k_max(array:list, k:int) -> list:
    # get the length of the array
    length = len(array)
    # check if k is greater or equal to the length of array
    if k >= length or k == 1: return [max(array)]
    
    length = length - k + 1
    # loop on each element
    for index in range(length):
        # modify the first n elements
        array[index] = max(array[index:index+k])
        
    return array[0:length]


print(find_each_k_max([10, 5, 2, 7, 8, 7], 2))
print(find_each_k_max([10, 5, 2, 7, 8, 7], 3))
print(find_each_k_max([10, 5, 2, 7, 8, 7], 4))
print(find_each_k_max([10, 5, 2, 7, 8, 7], 5))
print(find_each_k_max([10, 5, 2, 7, 8, 7], 6))