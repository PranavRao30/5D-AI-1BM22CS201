import random
import math

def simanl(ini, initemp, cr, it):
    # Initialize the current state, best state, and best cost
    curr = ini
    bstate = curr
    bcost = obj(curr)  
    temp = initemp 

    # Continue until the temperature is above 1
    while temp > 1:
        # Perform iterations at the current temperature
        for i in range(it):
            nst = neighbour(curr)
            currcost = obj(curr)  
            ncost = obj(nst) 

            # Decide whether to accept the neighbor based on the acceptance probability
            if ap(currcost, ncost, temp) > random.random():
                curr = nst 
            
            # Update the best state and best cost if the new cost is better
            if ncost < bcost:
                bstate = nst
                bcost = ncost

        # Cool down the temperature
        temp *= cr

    return bstate, bcost 

def obj(state):
    # Objective function: Calculate the cost (sum of squares)
    cost = 0
    for ele in state:
        cost += ele**2  
    return cost

def neighbour(state):
    # Generate a neighbor state by slightly modifying one element
    nstate = state.copy()  
    ind = random.randint(0, len(state) - 1)  
    nstate[ind] += random.uniform(-1, 1) 
    return nstate

def ap(curr, ncost, temp):
    # Acceptance probability function
    if(ncost < curr):
        return 1 
    return math.exp((curr - ncost) / temp) 

# main function
print(simanl([1, 2, 3, 4, 5], 1000, 0.99, 100))
