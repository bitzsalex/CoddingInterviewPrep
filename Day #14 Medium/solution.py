import random

def monte_carlo_simulator(count:int, radius:int=1) -> float:
    # return Non if the radius is zero
    if radius == 0:
        return None
    
    # initiate the points in the circle counter
    points_in_the_circle = 0
    
    # loop for the specified number of time
    for _ in range(count):
        # get random values for x and y
        # random.randint isn't working as intended, random.uniform is the way togo
        x, y = (random.uniform(-radius, radius), random.uniform(-radius, radius))
        # calculate the point position
        point_position = (x ** 2) + (y ** 2)
        
        # check if the point is inside the circle
        # if yes increase the counter by one
        if point_position <= (radius ** 2):
            points_in_the_circle += 1
            
    # return the estimated value of pi
    return round(4 * points_in_the_circle / count, 3)
        
        
print(monte_carlo_simulator(100000, 10))