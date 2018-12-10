<<<<<<< HEAD
=======
from collections import OrderedDict


#The main assumption that we will be making for our backtracking search is that
#all the runway times are going to be kept in order (i.e. the earlier planes are
#before the later planes

#TODO:In one of the edge cases discussed below, we need to add dates to each of 
#these plane leave times. The dict will have values that contain the the time and
#the dates. (e.g. ("PlaneOne",(1000, "12/01/05"))), find a way to compare dates
#(i.e. RegEx), and fix the edge case
planeLeaveTimes = OrderedDict([
	("PlaneOne", 1000), 
	("PlaneTwo", 1000), 
	("PlaneThree", 1000), 
	("PlaneFour", 1030), 
	("PlaneFive",1100)
	])

    
planes = ["PlaneOne", "PlaneTwo", "PlaneThree", "PlaneFour", "PlaneFive"]
runways = ["One", "Two", "Three"]

#currently, our CSP has the names of the planes as the variables, 
#a dictionary called planeLeaveTimes which has the
#departure times of the planes, and the runway names as the domain. 
#The avail of the runways will be tracked by a dictionary, self.runwayCheck.
class CSP:
    def __init__(self,variables,planeLeaveTimes,domain,count = 0):
        self.variables = variables
        self.planeLeaveTimes = planeLeaveTimes
        self.domain = domain
        self.runwayCheck = {}
        for runway in self.domain:
        	self.runwayCheck[runway] = 0

        #this will be used to check the number 
        #of times we needed to backtrack
        #during the algorithm
        self.count = count

def backtracking_search(csp):
    output = OrderedDict()
    return recursive_backtracking(output, csp)

#Edge cases to take care of:
#if there are absolutely no options (i.e. no possible solutions
#current)

#A pretty big problem: How do we track if a runway is free 
#today at 0005 or tomorrow at 0005? We need dates with each plane and
#when each runway is free

def recursive_backtracking(assignment, csp):
	if(len(assignment) == len(csp.variables)):
		return assignment

	for plane in reversed(csp.variables):
		if plane not in assignment:
			current = plane

	for runway in csp.domain:

		#Here, we are comparing when the runway time is free to the leave time of
		#the plane (e.g. if the plane currently on a runway last left at 1205, and 
		#the current plane leave time is past that, then the runway can be assigned
		#to that plane)
		if(csp.runwayCheck[runway] < csp.planeLeaveTimes[current]):
			assignment[current] = runway
			csp.runwayCheck[runway] = csp.planeLeaveTimes[current] + 5
			result = recursive_backtracking(assignment, csp)
			if result != False:
				return assignment
			assignment.pop(current,None)
		csp.count+=1
	#if the current plane has no more options, delay the plane by 5 minutes
	#by adding 5 to the plane leave time.
	return False


csp = CSP(planes, planeLeaveTimes, runways)
a = backtracking_search(csp)
print(csp.count)
print(a)
>>>>>>> 2da8c69d8598eaed287cb341195ee0c97d82c0b8
