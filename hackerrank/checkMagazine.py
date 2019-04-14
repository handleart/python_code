#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter



# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	#result = (Counter(note) - Counter(magazine)) 
	mDict = {}
	nDict = {}

	for i in magazine:
		if i not in mDict:
			mDict[i] = 0

		mDict[i] += 1

	for i in note:
		if i not in nDict:
			nDict[i] = 0

		nDict[i] += 1

	#print mDict, nDict
	for i in nDict:
		#print i
		if i not in mDict:
			return "No"

		#print nDict[i], mDict[i]
		if i in mDict and nDict[i] > mDict[i]:
			return "No"
	
	return "Yes"

def testcases():
	magazine = "give me one grand today night".rstrip().split()
	note = "give one grand today".rstrip().split()
	result = "Yes"
	print result == checkMagazine(magazine, note)

	magazine = "two times three is not four".rstrip().split()
	note = "two times two is four".rstrip().split()
	result = "No"
	print result ==  checkMagazine(magazine, note)

	magazine = "ive got a lovely bunch of coconuts".rstrip().split()
	note = "ive got some coconuts".rstrip().split()
	result = "No"
	print result == checkMagazine(magazine, note)

	magazine = "".rstrip().split()
	note = "".rstrip().split()
	result = "Yes"
	print result == checkMagazine(magazine, note)

	magazine = "Attack at dawn".rstrip().split()
	note = "attack at dawn".rstrip().split()
	result = "No"
	print result == checkMagazine(magazine, note)

	magazine = "check the words carefully in this sentence hope you check properly".rstrip().split()
	note = "words this properly check check".rstrip().split()
	result = "Yes"
	print result == checkMagazine(magazine, note)

	# magazine = "A".split()
	# note = "a".split()

	# for i in xrange(30000):
	# 	magazine += magazine
	# 	note += note

	# result = "No"
	# print result == checkMagazine(magazine, note)

if __name__ == '__main__':
    #m = int(mn[0])

    #n = int(mn[1])

    testcases()
