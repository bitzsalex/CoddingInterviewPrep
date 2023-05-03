from typing import List, Tuple, Set


def find_minimum_path(
    board:List[List[bool]], start:Tuple[int,int], end:Tuple[int,int]) -> int:
    """Minimum path finder

    Args:
        board (List[List[int]]): A list of list that contain booleans
        start (Tuple[int,int]): A starting position in (row, col)
        end (Tuple[int,int]): An ending position in (row, col)

    Returns:
        int: The minimum path from start position to end
    """
    return recursive_finder(board, start, end, set())


def recursive_finder(
    board:List[List[bool]], start:Tuple[int,int], end:Tuple[int,int], visited:Set) -> int:
    """A recursive function to find the minimum path

    Args:
        board (List[List[int]]): A board
        start (Tuple[int,int]): Starting position
        end (Tuple[int,int]): Ending position
        visited (Set): A set of visited paths so far

    Returns:
        int: The minimum path length from starting to ending position
    """
    if start == end:
        # return the number of visited paths, if start and end are equal
        return len(visited)
    
    path_lengths = []
    row, col = start
    visited = visited.union({start})
    
    # check if the top position is empty (walkable)
    if is_top_bottom_empty(board, start, visited):
        # walk the top position, if it is walkable
        path_lengths = append_to_paths(path_lengths, 
            recursive_finder(board, (row - 1, col), end, visited))
    # check if the right position is empty (walkable)
    if is_left_right_empty(board, start, visited, "right"):
        # walk the right position, it it is walkable
        path_lengths = append_to_paths(path_lengths, 
            recursive_finder(board, (row, col + 1), end, visited))
    # check if the bottom position is empty (walkable)
    if is_top_bottom_empty(board, start, visited, "bottom"):
        # walk the bottom position, it it is walkable
        path_lengths = append_to_paths(path_lengths, 
            recursive_finder(board, (row + 1, col), end, visited))
    # check if the left position is empty (walkable)
    if is_left_right_empty(board, start, visited):
        # walk the left position, it it is walkable
        path_lengths = append_to_paths(path_lengths, 
            recursive_finder(board, (row, col - 1), end, visited))
    
    # return the minimum value from all possible paths, else return 0 (if there is no path)
    return min(path_lengths) if len(path_lengths) else 0


def append_to_paths(path_lengths:List, value:int) -> list:
    """Append a value to a path lengths list

    Args:
        path_lengths (List): A list that contain already walked paths
        value (int): The value that supposed to be appended to path lengths

    Returns:
        list: Appended list
    """
    # check if the value is 0, if not append it
    if value: path_lengths.append(value)
    return path_lengths


def is_left_right_empty(
    board:List[List[bool]], position:Tuple[int,int],
    visited:Set, direction:str="left") -> bool:
    """Check if either the left or right position is walkable

    Args:
        board (List[List[bool]]): A board
        position (Tuple[int,int]): Current position
        visited (Set): A set of visited positions
        direction (str, optional): Which position to check, either left or right. Defaults to "left".

    Returns:
        bool: Returns True if it is walkable, False if not
    """
    row, col = position
    col = col - 1 if direction == "left" else col + 1
    return col != -1 and col < len(board[row]) and \
        (row, col) not in visited and not board[row][col]


def is_top_bottom_empty(
    board:List[List[bool]], position:Tuple[int,int],
    visited:Set, direction:str="top") -> bool:
    """Check if either the top or bottom position is walkable

    Args:
        board (List[List[bool]]): A board
        position (Tuple[int,int]): Current position
        visited (Set): A set of visited positions
        direction (str, optional): Which position to check, either top or bottom. Defaults to "top".

    Returns:
        bool: Returns True if it is walkable, False if not
    """
    row, col = position
    row = row - 1 if direction == "top" else row + 1
    return row != -1 and row < len(board) and \
        (row, col) not in visited and not board[row][col]


matrix = [[False, False, False, False],
          [True, True, False, True],
          [False, False, False, False],
          [False, False, False, False]]
assert find_minimum_path(matrix, (0, 0), (0, 0)) == 0, "The value must be 0"
assert find_minimum_path(matrix, (0, 1), (0, 0)) == 1, "The value must be 1"
assert find_minimum_path(matrix, (3, 0), (0, 0)) == 7, "The value must be 7"
assert find_minimum_path(matrix, (3, 0), (0, 3)) == 6, "The value must be 6"
assert find_minimum_path(matrix, (3, 2), (0, 2)) == 3, "The value must be 3"


matrix = [[False, False, False, False],
          [True, True, True, False],
          [False, False, False, False],
          [False, False, False, False]]
assert find_minimum_path(matrix, (0, 0), (0, 0)) == 0
assert find_minimum_path(matrix, (1, 0), (0, 0)) == 1
assert find_minimum_path(matrix, (3, 0), (0, 0)) == 9
assert find_minimum_path(matrix, (3, 0), (0, 3)) == 6
assert find_minimum_path(matrix, (2, 0), (3, 3)) == 4


matrix = [[False, False, False, False],
          [True, True, True, True],
          [False, False, False, False],
          [False, False, False, False]]
find_minimum_path(matrix, (3, 0), (0, 0))