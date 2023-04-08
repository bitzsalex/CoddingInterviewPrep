class NOrders:
    # accept the maximum length and implement circular array
    def __init__(self, max_length:int) -> None:
        # 
        self.last_index = max_length - 1
        # stores the current index
        self.current_index = 0
        # stores the last order ids
        self.ids = {}
        
    # the method that implement circular array
    def record(self, order_id:int):
        # store the id at the current index position
        self.ids[self.current_index] = order_id
        # reset the counter when you reached the last index
        self.current_index = self.current_index + 1 \
            if self.current_index < self.last_index else 0
    
    def get_last(self, index:int):
        return self.ids[
            # calculate the index to get the last element
            (self.current_index - index + self.last_index + 1) % self.last_index]
    
    
norders = NOrders(10)
for ids in range(10, 25):
    norders.record(ids)
    
norders.get_last(14)