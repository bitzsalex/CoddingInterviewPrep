from typing import List

def find_minimum_cost(mat:List[List]) -> int:
    minimum = min(mat[0])
    previous_index = mat[0].index(minimum)
    
    for i in range(1, len(mat)):
        curr_index = mat[i].index(
            min(mat[i][0:previous_index] + mat[i][previous_index+1:])
        )
        minimum += mat[i][curr_index]
        previous_index = curr_index
            
    return minimum


arr = [[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]]
find_minimum_cost(arr)