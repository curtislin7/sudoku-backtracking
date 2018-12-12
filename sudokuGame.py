from collections import OrderedDict

class sudokuBoard:
	def __init__(self):
		# self.board = [[0 for x in range(9)] for y in range(9)]
		self.board=[[3,0,6,5,0,8,4,0,0], 
		[5,2,0,0,0,0,0,0,0], 
		[0,8,7,0,0,0,0,3,1], 
		[0,0,3,0,1,0,0,8,0], 
		[9,0,0,8,6,3,0,0,5], 
		[0,5,0,0,9,0,6,0,0], 
		[1,3,0,0,0,0,2,5,0], 
		[0,0,0,0,0,0,0,7,4], 
		[0,0,5,2,0,6,3,0,0]]

		#[[3,0,6,5,0,8,4,0,0], 
		# [5,2,0,0,0,0,0,0,0], 
		# [0,8,7,0,0,0,0,3,1], 
		# [0,0,3,0,1,0,0,8,0], 
		# [9,0,0,8,6,3,0,0,5], 
		# [0,5,0,0,9,0,6,0,0], 
		# [1,3,0,0,0,0,2,5,0], 
		# [0,0,0,0,0,0,0,7,4], 
		# [0,0,5,2,0,6,3,0,0]]

		# [[3, 1, 6, 5, 7, 8, 4, 9, 2], 
		# [5, 2, 9, 1, 3, 4, 7, 6, 8], 
		# [4, 8, 7, 6, 2, 9, 5, 3, 1], 
		# [2, 6, 3, 4, 1, 5, 9, 8, 7], 
		# [9, 7, 4, 8, 6, 3, 1, 2, 5], 
		# [8, 5, 1, 7, 9, 2, 6, 4, 3], 
		# [1, 3, 8, 9, 4, 7, 2, 5, 6], 
		# [6, 9, 2, 3, 5, 1, 8, 7, 4], 
		# [7, 4, 5, 2, 8, 6, 3, 1, 9]]

		self.openPositions = []
		for row in range(9):
			for column in range(9):
				if(self.board[row][column] == 0):
					self.openPositions.append((row,column))
		self.count = 0
	
		# 
	def addNumber():
		pass

	def checkIfNumberOK(self, numberPosition, numberValue):

		xPosition = numberPosition[0]
		yPosition = numberPosition[1]
		print(yPosition)
		print(numberValue)

		#check row
		for rowCheckX in range(9):
			if(self.board[rowCheckX][yPosition] == numberValue):
				return False

		#check column
		for columnCheckY in range(9): 
			if(self.board[xPosition][columnCheckY] == numberValue):
				return False

		#miniBoardCheck
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

		return True

def backtracking_search(sudokuBoard):
    
    output = OrderedDict()

    return recursive_backtracking(output, sudokuBoard)


def recursive_backtracking(assignment, sudokuBoard):
    
    if(len(assignment) == len(sudokuBoard.openPositions)):
        return assignment
    
    for openPosition in reversed(sudokuBoard.openPositions):
        if openPosition not in assignment:
            current = openPosition 

    print(current)
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
    sudokuBoard.count+=1
    return False 

# test = sudokuBoard()
# a = backtracking_search(test)

test = sudokuBoard()
a = backtracking_search(test)
print(test.board)
print(a)