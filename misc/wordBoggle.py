# Boggle is a popular word game in which players attempt to 
#find words in sequences of adjacent letters on a rectangular board.

# Given a two-dimensional array board that represents the character 
#cells of the Boggle board and an array of unique strings words, 
#find all the possible words from words that can be formed on the board.

# Note that in Boggle when you're finding a word, 
#you can move from a cell to any of its 8 neighbors, 
#but you can't use the same cell twice in one word.

import copy 

inc = 0

# x > y ^ (x, y)
direction = [[-1, -1], [0, -1], [1, -1],
			 [-1, 0],  		    [1, 0],
			 [-1, 1],  [0, 1],  [1, 1]]

class TrieNode():
    def __init__(self, letter):
            self.letter = letter
            self.children = {}
            self.lastNode = False


def createTrie(root, p):
	currentTrieNode = root
	
	for letter in p: 
		if letter not in currentTrieNode.children:
			currentTrieNode.children[letter] = TrieNode(letter)

		currentTrieNode = currentTrieNode.children[letter]

	currentTrieNode.lastNode = True


def wordBoggle(board, words, debug = False):
	def xy(location):
		x = location[0]
		y = location[1]
		return x, y
	def inBoard(board, location):
		x, y = xy(location)

		if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
			return False
		else:
			return True

	def generateTrie(words):	
		root = TrieNode('')
		for w in words:
			createTrie(root, w)

		return root

	def findWord(root, location, word, visited, debug = False): 
		x, y = xy(location)
		letter = board[y][x]

		if debug: print 'letter', letter, visited[y][x]

		if visited[y][x] == 1:
			return False
		else:
			visited[y][x] = 1

		if root.letter != letter:
			return False

		word += root.letter
		if debug: print root.lastNode, word, root.letter, location, letter, root.children.keys(), location in visited
		if root.lastNode == True:
			found.add(word)

		
		for d in direction:
				newLocation = [x + y for x,y in zip(d, location)]
				xNew, yNew = xy(newLocation)

				if inBoard(board, newLocation) and board[yNew][xNew] in root.children.keys(): 
					newLetter =  root.children[board[yNew][xNew]].letter
					#print newLetter, root.children.keys(), newLocation
					v = copy.deepcopy(visited)
					
					findWord(root.children[newLetter], newLocation, word, v, debug)

	root = generateTrie(words)
	found = set()

	for y in xrange(len(board)):
		for x in xrange(len(board[0])):
			letter = board[y][x]
			#print letter
			#print letter, letter in root.children.keys()
			if letter in root.children.keys():
				findWord(root.children[letter], [x, y], '', [[0 for i in xrange(len(board[0]))] for i in xrange(len(board))], debug)
	
	return sorted(list(found))
	#exit()

def runTest(board, words, expectedResult):
	#print 'Passed' if result == findSubstrings(words, parts) else 'Failed'
	global inc
	inc += 1

	print inc
	

	output = wordBoggle(board, words) #longestPath(t)

	#print "result:", expectedResult, "output:", output

	if expectedResult == output:
		print 'Passed' 
	else:
		print 'Failed'
		print '----'
		print 'Expected result', expectedResult
		#output = sumSubsets(n, True)

		print 'output', wordBoggle(board, words, True)
		exit()


	print '---'

def testcases():
	board = [["R","L","D"], 
		     ["U","O","E"], 
		     ["C","S","O"]]
	words = ["CODE", 
			 "SOLO", 
			 "RULES", 
			 "COOL"]
	result = ["CODE", "RULES"]

	runTest(board, words, result)


	board = [["G","T"],
	  	     ["O","A"]]
	words = ["TOGGLE", 
	 		 "GOAT", 
			 "TOO", 
	 		 "GO"]

	

	result = ["GO", 
	 "GOAT"]

	runTest(board, words, result)

	board = [["A","X","V","W"], 
	 		 ["A","L","T","I"], 
			 ["T","T","J","R"]]
	words = ["AXOLOTL", 
	 "TAXA", 
	 "ABA", 
	 "VITA", 
	 "VITTA", 
	 "GO", 
	 "AXAL", 
	 "LATTE", 
	 "TALA", 
	 "RJ"]	

	result = ["AXAL", 
	 "RJ", 
	 "TALA", 
	 "TAXA", 
	 "VITTA"]

	runTest(board, words, result)

	board = [["A","X","V","W"], 
	 ["A","L","T","I"], 
	 ["T","T","J","R"]]
	words = ["AXOLOTL", 
	 "TAXA", 
	 "ABA", 
	 "VITA", 
	 "VITTA", 
	 "GO", 
	 "AXAL", 
	 "LATTE", 
	 "TALA", 
	 "RJ"]

	result = ["AXAL", 
		 "RJ", 
		 "TALA", 
		 "TAXA", 
		 "VITTA"]

	runTest(board, words, result)

 	board = [["A","B"],["C","D"]]
	wordords = []

	result = []

	runTest(board, words, result)

	board = [["S","A"], 
		 ["M","O"], 
		 ["W","E"], 
		 ["H","R"]]
	words = ["SOME", 
	 "DRONE", 
	 "WHERE", 
	 "SOMEWHERE", 
	 "WORD", 
	 "WE", 
	 "MORE"]

	result = ["SOME", "WE"]
	runTest(board, words, result)

if __name__ == '__main__':
	testcases()	
