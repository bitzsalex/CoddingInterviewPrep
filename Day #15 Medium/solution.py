import random


# I don't get what is the catch,
# I think we can solve such problem with built in method
def pick_one(stream:list) -> any:
    # use a random.choice method to return a random element
    return random.choice(stream)


# Just to get the concept behind, I googled and found the following solution
def pick_one_alternative(stream:list) -> any:
    # initialize two probability holding variables
    probability = last_probability = 0
    # a place to store the picked element
    picked_element = None
    
    # loop over the whole element
    for index in range(0, len(stream)):
        # estimate it's randomness
        probability = random.random()
        # check it's random probability is greater than the previous once
        if probability > last_probability:
            # if yes, pick the element
            picked_element = stream[index]
            
        # store the previous probability
        last_probability = probability
        
    # return the picked element
    return picked_element