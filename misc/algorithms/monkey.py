#methinks it is like a weasel
import random

def stringGenerator(size):
	char = 'abcdefghijklmnopqrstuvwxyz '
	#charList = list(char)

	string = []
	
	for i in xrange(size):
		rand = random.randint(0,len(char)-1)
		#print rand 
		#print rand
		string.append(char[rand])


	return string

def score(str1, str2):
	if (len(str1) != len(str2)):
		raise exception()

	score = 0
	matched = len(str1) * ['']

	#print matched

	for i in xrange(len(str1)):
		if str1[i] == str2[i]:
			#matched 
			score +=1
			matched[i] = str1[i]

	return score, matched

def monkeyDo(testString, length = 100):
	string = stringGenerator(len(testString))
	for i in xrange(length):
		iScore, matched = score(testString, string)

		if iScore == len(testString):
			print 'Success, counter: ', + i
			return matched


		else:
			for i in xrange(len(matched)):
				if matched[i] == '':
					matched[i] = stringGenerator(1)[0]

		string = matched


	return "Failed"

testString = 'methinks it is like a weasel'
testString = 'my name is art'
x = monkeyDo(list(testString), 100)
print "".join(x)
