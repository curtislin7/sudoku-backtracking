from collections import OrderedDict

class sudokuBoard:
	def __init__(self):
		#TODO: Add in our own randomized boards. 
		#TODO: Track the number backtracks with different "difficulties" of boards.
		#TODO: Graph the number of backtracks per board difficulty over x number of trials.

		# self.board = [[0 for x in range(9)] for y in range(9)]

		#This is our hardcoded practice board. 
		self.board=[[3,0,6,5,0,8,4,0,0], 
		[5,2,0,0,0,0,0,0,0], 
		[0,8,7,0,0,0,0,3,1], 
		[0,0,3,0,1,0,0,8,0], 
		[9,0,0,8,6,3,0,0,5], 
		[0,5,0,0,9,0,6,0,0], 
		[1,3,0,0,0,0,2,5,0], 
		[0,0,0,0,0,0,0,7,4], 
		[0,0,5,2,0,6,3,0,0]]

		#Output for our hardcoded practice board.
		# [[3, 1, 6, 5, 7, 8, 4, 9, 2], 
		# [5, 2, 9, 1, 3, 4, 7, 6, 8], 
		# [4, 8, 7, 6, 2, 9, 5, 3, 1], 
		# [2, 6, 3, 4, 1, 5, 9, 8, 7], 
		# [9, 7, 4, 8, 6, 3, 1, 2, 5], 
		# [8, 5, 1, 7, 9, 2, 6, 4, 3], 
		# [1, 3, 8, 9, 4, 7, 2, 5, 6], 
		# [6, 9, 2, 3, 5, 1, 8, 7, 4], 
		# [7, 4, 5, 2, 8, 6, 3, 1, 9]]

		#self.openPositions is a list that contains the positions of all the open
		#spaces indicated by 0 on the board. 
		self.openPositions = []
		for row in range(9):
			for column in range(9):
				if(self.board[row][column] == 0):
					self.openPositions.append((row,column))

		#self.count to track the number of backtracks we have.
		self.backtrackCount = 0
	
	#class function to check if adding a number to the board is ok, will return 
	#True if number is ok, and will return flase if number is not ok. numberPosition
	#is passed in as a tuple with the x position y position of the value, numberValue
	#is the value of the number itself.
	def checkIfNumberOK(self, numberPosition, numberValue):
		xPosition = numberPosition[0]
		yPosition = numberPosition[1]

		#check row by iterating through 0-8 with fixed y position
		for rowCheckX in range(9):
			if(self.board[rowCheckX][yPosition] == numberValue):
				return False

		#check column by iterating through 0-8 with fixed x position
		for columnCheckY in range(9): 
			if(self.board[xPosition][columnCheckY] == numberValue):
				return False

		#miniBoardCheck - check within the 3X3 "square" of the board to verify that
		#the numberValue is not already within the 3X3 board.
		miniBoardFirst = range(0,3)
		miniBoardSecond = range(3,6)
		miniBoardThird = range(6,9)
		miniBoardPosition = [0,0]

		if xPosition in miniBoardFirst:
			miniBoardPosition[0] = miniBoardFirst
		elif xPosition in miniBoardSecond:
			miniBoardPosition[0] = miniBoardSecond
		elif xPosition in miniBoardThird:
			miniBoardPosition[0] = miniBoardThird

		if yPosition in miniBoardFirst:
			miniBoardPosition[1] = miniBoardFirst
		elif yPosition in miniBoardSecond:
			miniBoardPosition[1] = miniBoardSecond
		elif yPosition in miniBoardThird:
			miniBoardPosition[1] = miniBoardThird

		for x in miniBoardPosition[0]:
			for y in miniBoardPosition[1]:
				if(self.board[x][y] == numberValue):
					return False

		#If all these conditions pass, then the number can be added safely without
		#violating any of the other rules.
		return True

	def displayBoard(self):
		# print("enter")
		for row in range(9):
			for column in range(9):
				if(column in [2,5]):
					print(self.board[row][column], "|", end = " ")
				else:
					print(self.board[row][column], end = " ")
			if(row in [2,5]):
				print("\n---------------------")
			else:
				print("")

def backtracking_search(sudokuBoard):
    output = OrderedDict()
    return recursive_backtracking(output, sudokuBoard)


def recursive_backtracking(assignment, sudokuBoard):
    
    #if all variables in sudokuBoard.openPositions have been assigned, end the recursion
    #and return.
    if(len(assignment) == len(sudokuBoard.openPositions)):
        return assignment
    
    #find the next unassigned open position in the board and make it the next one the 
    #algorithm assigns.
    for openPosition in reversed(sudokuBoard.openPositions):
        if openPosition not in assignment:
            current = openPosition 

    #Iterate through every possible value for the position. First, check that the number
    #does not violate any of the constraints placed upon it by sending it to the sudokuBoard
    #checkIfNumberOK function(i.e. no same number in row, column, or 3X3 area). If the number
    #does not violate any constraints, assign the current position to the number and modify the 
    #sudoku board. Continue recursion for the next number. If the result of the next number 
    #returns false, this means that none of the numbers could have worked for the next position
    #and we need to continue in the for loop to check if the next number will work. This is why
    #instead of returning the assignment, we remove the number we assigned to the position in 
    #the dictionary and rest the position on the board to 0.
    for number in range(1,10):
        checkNumber = sudokuBoard.checkIfNumberOK(current, number)
        if(checkNumber == True):
            assignment[current] = number
            sudokuBoard.board[current[0]][current[1]] = number
            result = recursive_backtracking(assignment, sudokuBoard)
            if result != False: 
                return assignment
            assignment.pop(current,None)
            sudokuBoard.board[current[0]][current[1]] = 0

    #If the algorithm reaches this point, none of the numbers in the for loop worked for the 
    #current position and we need to backtrack, so increment the backtrackCount.
    sudokuBoard.backtrackCount+=1
    return False 

# test = sudokuBoard()
# a = backtracking_search(test)

test = sudokuBoard()
a = backtracking_search(test)
test.displayBoard()