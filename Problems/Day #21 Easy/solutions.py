from typing import List, Tuple


def count_non_overlap(array:List, curr_index:int, counter:int, scheduled:List) -> int:
    length = len(array)
    
    # return 0 if it is empty
    if length == 0: return 0
    
    # return the cound if you are at the last index
    elif curr_index == length: return counter
    
    # head to the next element if it is already scheduled
    elif curr_index in scheduled:
        return count_non_overlap(array, curr_index+1, counter, scheduled)
    
    # take the end time as current maximum
    _, current_end = array[curr_index]
    
    # loop starting from next index till the end
    for index in range(curr_index + 1, length):
        # skip the element if it is in the scheduled list
        if index in scheduled: continue
        
        # get the start and end values
        start, end = array[index]
        # check if the start is greater than our current_end
        # if yes, they can be placed at the same class
        if start > current_end:
            # add the current index to scheduled list
            scheduled.append(index)
            # update the current_end value to look for another time interval
            # that can be grouped with the current ones
            current_end = end
    
    # update the counter and recurse until you reach the end
    return count_non_overlap(array, curr_index + 1, counter + 1, scheduled)

Schedule = Tuple[int, int]
Schdules = List[Schedule]

def get_non_overlapped(
    array:List, curr_index:int, counter:int, scheduled:List, schedules:Schdules) -> List[Schdules]:
    # same logic just like above, the difference is to return the groped schedules
    length = len(array)
    
    # return 0 if it is empty
    if length == 0: return []
    elif curr_index == length: return schedules
    elif curr_index in scheduled:
        return get_non_overlapped(array, curr_index+1, counter, scheduled, schedules)
    
    _, current_end = array[curr_index]
    current_group = [array[curr_index]]
    for index in range(curr_index + 1, length):
        if index in scheduled: continue
        
        start, end = array[index]
        if start > current_end:
            current_group.append(array[index])
            scheduled.append(index)
            current_end = end
    
    schedules.append(current_group)
    return get_non_overlapped(array, curr_index + 1, counter + 1, scheduled, schedules)



count_non_overlap([(30, 75), (0, 50), (60, 150)], 0, 0, []), \
get_non_overlapped([(30, 75), (0, 50), (60, 150)], 0, 0, [], [])

count_non_overlap([(15,50),(51,53),(54,58),(60,70),(61,63),(65,69),(71,83)], 0, 0, []), \
get_non_overlapped([(15,50),(51,53),(54,58),(60,70),(61,63),(65,69),(71,83)], 0, 0, [], [])

count_non_overlap([(1,3), (5,7), (9,11), (15,17)], 0, 0, []), \
get_non_overlapped([(1,3), (5,7), (9,11), (15,17)], 0, 0, [], [])

count_non_overlap([(1,10), (2,9), (3,8), (4,7), (5,6)], 0, 0, []), \
get_non_overlapped([(1,10), (2,9), (3,8), (4,7), (5,6)], 0, 0, [], [])

count_non_overlap([(1,10)], 0, 0, []), \
get_non_overlapped([(1,10)], 0, 0, [], [])

count_non_overlap([(1,3), (3,5), (6,9), (10,20)], 0, 0, []), \
get_non_overlapped([(1,3), (3,5), (6,9), (10,20)], 0, 0, [], [])

count_non_overlap([(0,10), (20,30), (40,50)], 0, 0, []), \
get_non_overlapped([(0,10), (20,30), (40,50)], 0, 0, [], [])

count_non_overlap([(1,10), (2,9), (3,8), (4,7), (5,6)], 0, 0, []), \
get_non_overlapped([(1,10), (2,9), (3,8), (4,7), (5,6)], 0, 0, [], [])

count_non_overlap([(1,10), (4,14), (8,18), (12,22), (16,26)], 0, 0, []), \
get_non_overlapped([(1,10), (4,14), (8,18), (12,22), (16,26)], 0, 0, [], [])

count_non_overlap([(1,6), (4,10), (8,14), (12,18), (16,22), (20,26), (24,30), (28,34)], 0, 0, []), \
get_non_overlapped([(1,6), (4,10), (8,14), (12,18), (16,22), (20,26), (24,30), (28,34)], 0, 0, [], [])

count_non_overlap([(1,5), (2,6), (3,7), (4,8), (5,9), (6,10), (7,11), (8,12)], 0, 0, []), \
get_non_overlapped([(1,5), (2,6), (3,7), (4,8), (5,9), (6,10), (7,11), (8,12)], 0, 0, [], [])
