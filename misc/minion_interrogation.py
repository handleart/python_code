#you decide to interrogate the minions in an order which will take the least expected time (you can only use the machine on one minion at a time).

#[time, numerator,  denominator]

#There will be at-least two and no more than 50 minions.
#All the integers in the input will be positive integers, no more than 1024.

import itertools
import random 

def answer(minions):
	i = 0;
	tmpMinions = []

	for m in minions:
		tmpMinions.append([i, float(m[0]) * float(m[2]) / float(m[1])]);
		i += 1


	tmpMinions = sorted(tmpMinions, key = lambda x: x[1])

	result = []

	for m in tmpMinions:
		result.append(m[0]);

	#print result

	return result

def answer_np(minions):
	i = 0;
	for m in minions:
		m.append(i)
		i += 1
		
	iterMinions = itertools.permutations(minions)

	i = 0;

	val = 0;
	for m in iterMinions:
		i = 0;
		prob = 1.;
		t = 0 ;
		old_t = 100000000;

		for arr in m:
			t += arr[0] * prob 
			prob = prob * ( 1 - float(arr[1]) / float(arr[2]))
			i += 1
		

		if old_t > t:
			result = []
			for i in m:
				result.append(i[3]); 


	return result


def test1():
	minions = [[5, 1, 5], [10, 1, 2]]
	ans = answer(minions);
	result = [1, 0]
	print ans == result


def test2():
	minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
	ans = answer(minions);

	result = [2, 3, 0, 1]
	print ans == result

def test3():
	minions = [[5, 1, 5], [10, 1, 2], [2, 5, 7]]
	ans = answer(minions);
	ans_np = answer_np(minions)
	result = [2, 1, 0]
	print ans
	#print ans_np
	#print result
	print ans == result

def test4():
	minions = [[5, 1, 5], [5, 1, 5], [5, 1, 10], [5, 1, 5] ]
	ans = answer(minions);
	result = [0, 1, 3, 2]
	print ans
	print ans == result


def test_perf():
	minions = []
	for i in xrange(50):
		a = random.randint(1,1024)
		b = random.randint(1,1024)
		c = random.randint(b,1024)

		minions.append([a, b, c])

	ans = answer(minions);

test1()
print "----"
test2()
print "----"
test3()
print "----"
test4()
print "----"
test_perf()

