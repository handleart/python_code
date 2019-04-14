#!/usr/bin/python
#Test cases
#==========

#Inputs:
#    (int) meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
#Output:
#    (int) 4

#Inputs:
#    (int) meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
#Output:
#    (int) 1

import random

def answer(meetings):
	sortedMeetings = sorted(meetings, key = lambda x: x[1])

	#maxNumOfMeetings(sortedMeetings)

	#define greedy algorithm

	#grab first start and end time
	#figure out which of the items in the list intersect with it and remove them from the list
	#grab the second item from the list that is still valid
	#do the same process for it
	#keep track of how many times the process was repeated

	tracker = len(sortedMeetings) * [1] 

	for i in xrange(0,len(sortedMeetings)):
		if tracker[i]:

			startTime = sortedMeetings[i][0]
			endTime = sortedMeetings[i][1]

			for j in xrange(i+1, len(sortedMeetings)):
				jStart = sortedMeetings[j][0]
				jEnd = sortedMeetings[j][1]

				if jStart < endTime:
					#print sortedMeetings[j]
					tracker[j] = 0;


	print sortedMeetings
	#print tracker

	return  sum(tracker)

def answer2(meetings):
	sortedMeetings = sorted(meetings, key = lambda x: x[1])

	#maxNumOfMeetings(sortedMeetings)

	#define greedy algorithm

	#grab first start and end time
	#figure out which of the items in the list intersect with it and remove them from the list
	#grab the second item from the list that is still valid
	#do the same process for it
	#keep track of how many times the process was repeated 
	length = 1

	maxVal = sortedMeetings[0][1]
	for i in xrange(1,len(sortedMeetings)):
		if sortedMeetings[i][0] >= maxVal:
			length += 1


			maxVal = sortedMeetings[i][1]


	#print sortedMeetings

	return length

meetings = {}
meetings[0] = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]];

meetings[1] = [[0, 1], [1, 2], [3, 5], [4, 5], [2, 3], [2,5]];
meetings[2] = [[2, 5], [0, 1], [1, 2], [3, 5], [4, 5], [2, 3], [2,5]];
meetings[3] = [[2, 5], [0, 1], [1, 2], [1, 3], [3, 5], [4, 5], [2, 3], [2,5]];
meetings[4] = [[0, 1000000], [42, 43], [0, 1000000], [42, 43], [0, 41]];
meetings[5] = [[0, 50], [51, 70], [20, 40], [10, 20], [60, 70]];
meetings[6] = [[0, 50], [51, 70], [21, 40], [10, 20], [60, 70], [0, 40]];
meetings[7] = [[0, 50], [51, 70], [21, 40], [10, 20], [60, 70], [0, 40], [63, 65]];
meetings[8] = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]

meetings[9] = []
for i in xrange(0,101):
	z = random.randrange(0,1000000)
	meetings[9].append([random.randrange(0,z), z])

meetings[10] = []
for i in xrange(0,10):
	z = random.randrange(0,1000000)
	meetings[10].append([random.randrange(0,z), z])


meetings[11] = [[0, 1], [0, 1], [0, 1], [0, 1]]

meetings[12] = [[0,1]] * 1000
meetings[12].append([2,3])

meetings[13] = []
for i in xrange(0,101):
	meetings[13].append([i, i+1])

for m in meetings:
	#val1 = answer(meetings[m]);
	

	val2 = answer2(meetings[m]);

	#if (val1 != val2):
	#print "Answer1: " + str(val1)
	#print "Answer2: " + str(val2)
		

#meetings = [[2, 5], [0, 1], [1, 2], [1, 3], [3, 5], [4, 5], [2, 3], [2,5]];
#meetings = [[0, ], [1, 2], [1,3], ]



#sort all the items using the second item in list
#	
