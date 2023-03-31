number = 4
possible_moves = [1, 2]

class Counter:
    def __init__(self, number:int, move_sets:list) -> None:
        self.number = number
        self.possible_moves = move_sets
        self.count = 0
        
    def change_moves_set(self, move_sets:list) -> None:
        self.possible_moves = move_sets
        
    def the_counter(self, current_sum:int=0) -> None:
        for element in self.possible_moves:
            if element + current_sum < self.number:
                self.the_counter(current_sum + element)
            elif (element + current_sum) == self.number:
                self.count += 1
        
    def count_moves(self) -> int:
        self.count = 0
        self.the_counter()
        return self.count
                

counter = Counter(number, move_sets=possible_moves)
counter.count_moves()
counter.change_moves_set([1, 3, 5])
counter.count_moves()