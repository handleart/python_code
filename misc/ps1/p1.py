
# In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. 
# lsDownload the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]
# ...
# For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. 
# You should NOT assume that edge weights or lengths are distinct.

# Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). 
# Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

# ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum)!

#first value weight, second value length
def p1(input_val):
	sorted_input = sorted(input_val, key=lambda x: (-x[0] + x[1], -x[0]))

	#print sorted_input
	#weighted complete times
	l = 0
	result = 0 


	for i in sorted_input:
		l += i[1]
		result = result + l * i[0]



	return result

def p2(input_val):

	sorted_input = sorted(input_val, key=lambda x: (- float(x[0]) / float(x[1]), -x[0]))


	#weighted complete times

	l = 0
	result = 0 

	for i in sorted_input:
		l += i[1]

		result = result + l * i[0]
	return result 


def run_script():
	jobs = []
	i = 0

	with open('jobs.txt') as inputfile:
	    for line in inputfile:
	    	#if i > 0 and i < 10:
	    	if i > 0:
	         tmp = line.strip().split()
	         jobs.append([int(tmp[0]), int(tmp[1])]);	        
	        
	        i += 1

	print "W - L ", p1(jobs)
	print "W / L ", p2(jobs)

def test1():
	jobs = [[1, 1], [1, 2], [2, 1]];

	result = [[1, 2], [1, 1], [2, 1]]
	print "Test1",
	tmp = [[1, 1], [1, 2], [2, 1]];
	print result == p1(jobs)

	print p1(jobs)

def test2():
	jobs = [[1, 1], [1, 2], [2, 1], [3, 2]];

	result = [[1, 2], [1, 1], [3,2], [2, 1]]

	print "Test2",
	print result == p1(jobs)

	print p1(jobs)


def test3():
	jobs = [[3, 5], [1,2]]

	print p1(jobs)
	print p2(jobs)

run_script()
#test3()
#test2()
