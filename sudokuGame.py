from collections import OrderedDict
import random
import time

class sudokuBoard:
	def __init__(self, board = None):
		#Generate a random board that has a minimum of 17 clues(any number less than this will
		#not have a unique solution), according to math.
		self.board = board
		if(board == None):
			self.numberOfFilledPositions = 0
			while(self.numberOfFilledPositions<17):
				self.numberOfFilledPositions = 0
				self.board = [[0 for x in range(9)] for y in range(9)]
				self.generateRandomBoard()
			self.initialBoard = self.board
		else:
			self.initialBoard = self.board

		#self.openPositions is a list that contains the positions of all the open
		#spaces indicated by 0 on the board. 
		self.openPositions = []
		for row in range(9):
			for column in range(9):
				if(self.board[row][column] == 0):
					self.openPositions.append((row,column))

		#self.count to track the number of backtracks we have.
		self.backtrackCount = 0

	def generateRandomBoard(self):
		for row in range(9):
			numberRandomInRow = random.randint(1,3)
			randomIndices = random.sample(range(0, 9), numberRandomInRow)
			self.numberOfFilledPositions += numberRandomInRow
			for randomColumn in randomIndices:
				numberPosition = (row, randomColumn)
				while(self.board[row][randomColumn] == 0):
					randomNumber = random.randint(1,9)
					if(self.checkIfNumberOK(numberPosition, randomNumber)):
						self.board[row][randomColumn] = randomNumber

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

	#The main assumption for this function is if a board is returned with any 
	#unfilled values(i.e. a number value of 0 in the returned board, it will 
	#mean that our algorithm failed and no solution was
	#found for the given Sudoku board.
	def checkIfBoardOK(self):
		for row in range(9):
			for column in range(9):
				if(self.board[row][column] == 0):
					return False
		return True

	#Function to iterate through our 2d array and print our values in a "pretty"
	#fashion.
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

def runTestsDisplay(numberOfTests):
	for i in range(numberOfTests):
		print("New Sudoku Test:", i)
		sudokuTest = sudokuBoard()
		print("Number of clues given for randomly generated sudoku board:", sudokuTest.numberOfFilledPositions)
		print("")
		print("Randomly generated sudoku board:")
		sudokuTest.displayBoard()
		startTime = time.time()
		a = backtracking_search(sudokuTest)
		endTime = time.time()
		runTime = endTime-startTime
		if(sudokuTest.checkIfBoardOK()):
			print("Solution for sudoku board:")
		else:
			print("There is no solution for this board.")
		sudokuTest.displayBoard()
		print("Runtime of backtracking algorithm:", runTime)
		print("Number of backtracks for sudoku board:", sudokuTest.backtrackCount)

def displayBoardInformation(boardResults):
	# print("Number of Clues Given     Sudoku Solved?     Algorithm Runtime:     Number of Backtracks:")
	for item in boardResults:
		print(item, end = " ")
	print("")

def runTests(numberOfTests):
	boardResults = []
	for i in range(numberOfTests):
		# print("Running test ", i+1)
		boardInformation = []
		sudokuTest = sudokuBoard()
		boardInformation.append(sudokuTest.numberOfFilledPositions)
		startTime = time.time()
		a = backtracking_search(sudokuTest)
		endTime = time.time()
		runTime = endTime-startTime
		if(sudokuTest.checkIfBoardOK()):
			boardInformation.append("Yes")
		else:
			boardInformation.append("No")
		boardInformation.append(runTime)
		boardInformation.append(sudokuTest.backtrackCount)
		# boardResults.append(boardInformation)
		# sudokuTest.displayBoard()
		displayBoardInformation(boardInformation)

#This function will run multiple tests with randomly generated boards. 
#Fortunately, if the randomly generated board is too "hard", the algorithm
#will keep running until it finds a solution, or fails. For this reason, 
#it can take a VERY long time to run these tests, as some sudoku boards 
#will run the algorithm for upwards of 80 seconds. If this happens and you 
#are very impatient, just run them again, or input a hardcoded board.
# runTestsDisplay(5)

#Test 1 - Practice Board
print("Test 1 - Hardcoded Practice Board")
practiceBoard=[[3,0,6,5,0,8,4,0,0], 
		[5,2,0,0,0,0,0,0,0], 
		[0,8,7,0,0,0,0,3,1], 
		[0,0,3,0,1,0,0,8,0], 
		[9,0,0,8,6,3,0,0,5], 
		[0,5,0,0,9,0,6,0,0], 
		[1,3,0,0,0,0,2,5,0], 
		[0,0,0,0,0,0,0,7,4], 
		[0,0,5,2,0,6,3,0,0]]

sudokuTest = sudokuBoard(practiceBoard)

print("Initial Input Board:")
sudokuTest.displayBoard()
startTime = time.time()
a = backtracking_search(sudokuTest)
endTime = time.time()
runTime = endTime-startTime
if(sudokuTest.checkIfBoardOK()):
	print("Solution for sudoku board:")
else:
	print("There is no solution for this board.")
sudokuTest.displayBoard()
print("Runtime of backtracking algorithm:", runTime)
print("Number of backtracks for sudoku board:", sudokuTest.backtrackCount)

#Test 2 - Hard Sudoku Board("Platinum Blonde")
#This is a famously very hard Sudoku board that we have hardcoded for our algorithm
#to solve. "This ultra-difficult puzzle (the lower puzzle in the above image) had a 
#difficulty of 3.5789 on the Richter scale..."
#https://www.cbsnews.com/news/mathematicians-create-richter-scale-of-sudoku-difficulty/
print("Test 2 - Platinum Blonde Super Hard Board")
platinumBlonde=[[8,0,0,0,0,0,0,0,0],
		[0,0,3,6,0,0,0,0,0],
		[0,7,0,0,9,0,2,0,0],
		[0,5,0,0,0,7,0,0,0],
		[0,0,0,0,4,5,7,0,0],
		[0,0,0,1,0,0,0,3,0],
		[0,0,1,0,0,0,0,6,8],
		[0,0,8,5,0,0,0,1,0],
		[0,9,0,0,0,0,4,0,0]]

sudokuTest = sudokuBoard(platinumBlonde)

print("Initial Input Board:")
sudokuTest.displayBoard()
startTime = time.time()
a = backtracking_search(sudokuTest)
endTime = time.time()
runTime = endTime-startTime
if(sudokuTest.checkIfBoardOK()):
	print("Solution for sudoku board:")
else:
	print("There is no solution for this board.")
sudokuTest.displayBoard()
print("Runtime of backtracking algorithm:", runTime)
print("Number of backtracks for sudoku board:", sudokuTest.backtrackCount)

#Test 3 - Multiple Tests With Randomly Generated Boards
#This function will run multiple tests with randomly generated boards. 
#Fortunately, if the randomly generated board is too "hard", the algorithm
#will keep running until it finds a solution, or fails. For this reason, 
#it can take a VERY long time to run these tests, as some sudoku boards 
#will run the algorithm for upwards of 80 seconds. If this happens and you 
#are very impatient, just run them again, or input a hardcoded board.
runTestsDisplay(5)
