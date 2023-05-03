from typing import List

def find_minimum_cost(mat:List[List]) -> int:
    # take the minimum of the first row
    minimum = min(mat[0])
    # get the index of the first row element
    previous_index = mat[0].index(minimum)
    
    # loop in a row wise
    for i in range(1, len(mat)):
        # split the current row cost list to exclude the previous minimum index
        # then find the minimum
        curr_index = mat[i].index(
            min(mat[i][0:previous_index] + mat[i][previous_index+1:])
        )
        # add the minimum costs
        minimum += mat[i][curr_index]
        # change the previous_index to the current minimum index
        previous_index = curr_index
            
    return minimum


arr = [[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]]
find_minimum_cost(arr)
find_minimum_cost([[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6]])
find_minimum_cost([[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]])