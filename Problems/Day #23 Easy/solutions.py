from typing import List, Tuple


class PathFinder:
    def __init__(self, board:List[List[bool]]):
        self.board = board

    def find_minimum_path(self, start:Tuple, end:Tuple) -> int:
        if len(start) != 2 or len(end) != 2: return None
        return self.find_path(start, end, set())

    def is_vertical_empty(self, current:Tuple, visited:set, place:str="top") -> bool:
        x = current[0] - 1 if place == "top" else current[0] + 1
        coordinate = (x, current[1])
        return not (
            x == -1 or x >= len(self.board) or self.board[x][current[1]] or coordinate in visited
            )

    def is_horizontal_empty(self, current:Tuple, visited:set, place:str="left") -> bool:
        y = current[1] - 1 if place == "left" else current[1] + 1
        coordinate = (current[0], y)
        return not (
            y == -1 or y >= len(self.board[0]) or self.board[current[0]][y] or coordinate in visited
            )
        
    def add_path_length(self, path_lengths:List, path_length:int) -> None:
        if path_length != 0:
            path_lengths.append(path_length)
            
        return path_lengths
     
    def find_path(self, start:Tuple, end:Tuple, visited:set) -> int:
        if start == end: return len(visited)
        
        path_lengths = []
        print(start, visited)
        if self.is_horizontal_empty(start, visited):
            path_lengths.append(self.find_path((start[0], start[1] - 1), end, visited.union({start})))
        if self.is_vertical_empty(start, visited):
            path_lengths.append(self.find_path((start[0] - 1, start[1]), end, visited.union({start})))
        if self.is_horizontal_empty(start, visited, "right"):
            path_lengths.append(self.find_path((start[0], start[1] + 1), end, visited.union({start})))
        if self.is_vertical_empty(start, visited, "bottom"):
            path_lengths.append(self.find_path((start[0] + 1, start[1]), end, visited.union({start})))
        
        return min(path_lengths) + 1 if len(path_lengths) else 0


matrix = [[False, False, False, False],
          [True, True, False, True],
          [False, False, False, False],
          [False, False, False, False]]

finder = PathFinder(matrix)

finder.find_minimum_path((1, 0), (0, 0))

assert finder.find_minimum_path((0, 0), (0, 0)) == 0, "The value must be 0"
assert finder.find_minimum_path((1, 0), (0, 0)) == 1, "The value must be 1"
assert finder.find_minimum_path((3, 0), (0, 0)) == 7, "The value must be 7"
assert finder.find_minimum_path((3, 0), (0, 3)) == 6, "The value must be 6"

matrix = [[False, False, False, False],
          [True, True, True, False],
          [False, False, False, False],
          [False, False, False, False]]

finder = PathFinder(matrix)

assert finder.find_minimum_path((0, 0), (0, 0)) == 0
assert finder.find_minimum_path((1, 0), (0, 0)) == 1
assert finder.find_minimum_path((3, 0), (0, 0)) == 9
assert finder.find_minimum_path((3, 0), (0, 3)) == 6
assert finder.find_minimum_path((2, 0), (3, 3)) == 4


check = {1, 2, 6}
type(check)
check.union({5})
check 