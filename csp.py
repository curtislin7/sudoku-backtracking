from collections import OrderedDict


#The main assumption that we will be making for our backtracking search is that
#all the runway times are going to be kept in order (i.e. the earlier planes are
#before the later planes

planeLeaveTimes = OrderedDict([
	("PlaneOne",1000), 
	("PlaneTwo",1000), 
	("PlaneThree", 1020), 
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
#if the time is past midnight, rest back to 0
#if there are absolutely no options (i.e. no possible solutions
#current )
def recursive_backtracking(assignment, csp):
	if(len(assignment) == len(csp.variables)):
		return assignment

	for plane in reversed(csp.variables):
		if plane not in assignment:
			current = plane

	for runway in csp.domain:
		isOK = True
		if(csp.runwayCheck[runway] >= csp.planeLeaveTimes[current]):
			isOK = False
		if(isOK == True):
			assignment[current] = runway
			csp.runwayCheck[runway] = csp.planeLeaveTimes[current] + 5
			result = recursive_backtracking(assignment, csp)
			if result != False:
				return assignment
			assignment.pop(current,None)
		csp.count+=1
	#if the current plane has no more options, delay the plane by 5 minutes
	#by adding 5 to the plane leave time
	return False


csp = CSP(planes, planeLeaveTimes, runways)
a = backtracking_search(csp)
print(csp.count)
print(a)