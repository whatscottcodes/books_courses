###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cows_under_limit = dict(cows) #can't mutate cows, so we make a copy
    #iterate through cows and remove any cows with a weight over the limit
    for cow in cows:
        if cows_under_limit[cow] > limit:
            del cows_under_limit[cow]
    #cowsSorted is a list of the dictionary keys (names of cows) 
    #sorted by the associated values, the values are not recorded in the list.            
    cowsSorted = sorted(cows_under_limit,key=cows.get,reverse=True)
    all_trips = []
    while True:
        
        trip = []
        currentWeight = 0
        for i in cowsSorted: #iterate through sorted cows
            #add the cow name to trip if adding it to the current weight is less than the limit
            if currentWeight + cows[i] <= limit:
                trip.append(i)
                currentWeight += cows[i] #keep track of the current weight in the ship
        
        all_trips.append(trip) #after iterating through the whole list, we have a trip
        #append the trip to our list of all trips
        cowsLeft = [] 
        for i in cowsSorted:
            if i not in trip: #if our cow in cowsorted is not in our current trip
               cowsLeft.append(i)  #we append it to cowsLeft which is a temp list essentially
        cowsSorted = cowsLeft #update our cowsSorted list to the cowsLeft
        if cowsSorted == []: #when cowsSorted is empty, we've shipped all the cows we can
            break

    return all_trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    all_sets_of_trips = []
    #partition returns all patritions - aka all sets of trips that
    #transport all cows from earth to space, we name this list of all sets "all_sets_of_trips"
    for part in get_partitions(cows.keys()):
        all_sets_of_trips.append(part)
    
    all_trip_sets = []    
    #iterate through all the sets of trips, so i is one set
    #that is a list of trips that gets all cows off the planet
    for i in range(len(all_sets_of_trips)): 
        trip = []
        for j in range(len(all_sets_of_trips[i])): #j is looking at an individual trip in set i
        #so i=1, j=0 looks at the first trip of the second set, i=1,j=1 looks at the second trip in that second set
            weight_of_trip = []
            for k in all_sets_of_trips[i][j]: #k is looking at the individual cows on trip j in set i
                weight_of_trip.append(cows[k]) #appends the value (weight) of the cow, represented by k, from cows
                #so weight_of_trip is a list of weights of the cows on trip j in set i
            if sum(weight_of_trip) > limit: #if the sum of a trip(j) is over the limit, break out of the loop
                break
            trip.append(all_sets_of_trips[i][j]) #appends that jth list of the ith key of trips to trip
        if len(trip) == len(all_sets_of_trips[i]): #checks to see if we actually made it through the whole set of trips(i)
        #if we did then we add it to all trips
        #this entire process is just weeding out and sets of trips(i) that include trips(j) that exceed our limit
        #and are therefore impossible
            all_trip_sets.append(trip)
            
    number_of_trips = []        
    #creates a list of just the number of trips per set
    for i in range(len(all_trip_sets)):
        total.append(len(all_trip_sets[i]))
              
    for scenario in all_trip_sets:
        #checks if the length of a set i in the all_trips list is equal
        #to the minimum value in our list of trip lengths
        #if it is, that is our set with the least amount of trips
        #and we return it
        if len(scenario) == min(number_of_trips):
            return scenario #because it is the first scenario to match the lowest number of trips in a set
                            #that gets all the cows off the planet

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


