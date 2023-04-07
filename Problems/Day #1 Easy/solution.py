# first idea
example_list = [10, 15, 3, 7]
k = 17
length = len(example_list)


def method_one(num_list, k):
    # loop twice in a forward manner and compare the sum with k
    for index, item in enumerate(num_list):
        for inner in range(index + 1, length):
            if k == (item + num_list[inner]): return True

    return False


print(method_one(example_list, k))


# using itertools
import itertools

def method_two(num_list, k):
    # make any possible combination of two items
    combinations = itertools.combinations(num_list, 2)
    for combination in combinations:
        if sum(combination) == k: return True
    
    return False


print(method_two(example_list, k))


# Modification
# =================
def method_three(num_list, k):
    # loop twice in a forward manner and compare the sum with k
    for index, item in enumerate(num_list):
        for inner in range(index + 1, length):
            if k == (item + num_list[inner]): return [index, inner]

    return None


print(method_three(example_list, k))


# using itertools
def method_four(num_list, k):
    # make any possible combination of two items
    combinations = itertools.combinations(num_list, 2)
    for combination in combinations:
        if sum(combination) == k:
            return [num_list.index(num) for num in combination]
    
    return None


print(method_four(example_list, k))