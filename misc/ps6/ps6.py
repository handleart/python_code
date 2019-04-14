'''
HW 6: Algorithms

Question 1
In this assignment you will implement one or more algorithms for the 2SAT problem. 
Here are 6 different 2SAT instances: #1 #2 #3 #4 #5 #6.
The file format is as follows. In each instance, the number of variables and the number of clauses is the same,
 and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two 
 literals, with a number denoting the variable and a "-" sign denoting logical "not".
  For example, the second line of the first data file is "-16808 75250", which indicates the clause 
  -x16808vx75250.

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. 
In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, 
and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, 
then you should enter the string 111000 in the box below.

DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want. 
For example, 2SAT reduces to computing the strongly connected components of a suitable graph
 (with two vertices per variable and two directed edges per clause, you should think through the details). 
 This might be an especially attractive option for those of you who coded up an SCC algorithm for my Algo 1 course. 

 Alternatively, you can use Papadimitriou's randomized local search algorithm. 

 (The algorithm from lecture is probably too slow as stated, so you might want to make one or more simple 
 	modifications to it --- even if this means breaking the analysis given in lecture --- 
 	to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. 
In lecture we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, 
for example, for more details.

The variables are X1 through X4. So, the first clause is X1 or X2.  So, its
standard use is V symbol to denote logical OR.  So, what this clause means is
that its satisfied if either X1 is true or if X2  is true. The only way you
can screw up satisfying  this clause is by setting both X1 and and X2 to
false.  The next clause has the form not-X1 or X3.  The only way you can screw
up satisfying this clause is by setting X1 to be true  and X3 to be false.
Then we're going to have a clause x3 or  x4. Again this is satisfied unless
you wind  up setting x3 and x4 both to be false. And then finally we have a
clause not x2  or not x4. And this is satisfied except in the case  that you
assign both x2 and x4 to be true.  '''


from os import path, listdir
import math
import random
import itertools
from collections import defaultdict
import time

#Function to read file 
def readFile(fPath, f):
	k = 0
	result = set()
	with open(path.join(fPath, f), 'r') as f:
		next(f)
		for row in f:
			try:
				k +=1
				x, y = map(int, row.strip('').split(' '))

				result.add((x, y))

				#if k > 10: break
			except Exception as e:
				print e, row
				raise Exception

	return result


#Function to reduce data based on 
def reduceDataPairsFunc(data):
	"""
	Suggestion on the discussion forum:

	Given all the clauses of a 2SAT problem, remove the clauses that include
	a variable which has only one form (itself or its negation) in all clauses.
	Because of the singular form of such variables, having the form to be true
	means having the clauses containing this form to be true, thus those clauses
	can be removed without affecting the original 2SAT problem.
	For example:
	1, -3
	2, 1
	1, 4
	-2, 3
	-3, 2
	can be reduced to
	-2, 3
	-3, 2
	because variable 1 has on negation in all clauses, we just set it to be true,
	then the first three clauses are true and can be ignored.
	Note that after one iteration of reduction, some variables that are not
	singular prior to reduction can become singular afterwards, thus reduction
	should be done iteratively until no singular variables exist.

	D carries each set associated to a value
	tmpData is a copy of the data set
	"""

	D = defaultdict(set)

	for d1, d2 in data:
		D[d1].add((d1, d2))
		D[d2].add((d1, d2))

	tmpData = set(data)

	while True:
		var = set(itertools.chain(*tmpData))
		reducedVar = [i for i in var if -i not in var]

		for j in reducedVar: 
			tmpData -= D[j]
	
		#reducedVar = set()

		if not reducedVar:
			break

	return tmpData 

def papadimitriou(data):
	variables = set(map(abs, itertools.chain(*data)))
	n = len(variables)
	#print n, int(math.log(n, 2)), 2 * int(n) ** 2
	D = {}

	for i in xrange(int(math.log(n, 2))):
		#choose random initial assigment
		D = {}
		for i in variables:
			D[i] = random.choice([True, False])
			D[-i] = not D[i]

		#for j in xrange(2 * pow(n, 2)) :
		for j in xrange(2 * n ** 2) :
			false_vars = check_false_pairs(D, data)
			if not false_vars:
				return '1'
			else:
				D = flipChoice(D, false_vars)

	return '0'

def check_false_pairs(D, data):
	return [x for x in data if not (D[x[0]] | D[x[1]])]
	
def flipChoice(D, false_vars):
	flip_vars = random.choice(list(false_vars))
	flip_var = random.choice(flip_vars)
	D[flip_var] = not D[flip_var]
	D[-flip_var] = not D[-flip_var]

	return D


def runPS6():
	result = ''

	filesPath = 'data/'
	#testFile = 'testdata.txt'
	files = [i for i in listdir(filesPath) if path.isfile(path.join(filesPath, i))]
	#files = ['2sat1.txt', '2sat2.txt', '2sat3.txt']
	#files = ['2sat3.txt']

	for f in files:
		startTime = time.time()
		data = readFile(filesPath, f)
		reducedData = reduceDataPairsFunc(data)
		n = len(reducedData)

		print n, ", Time to read file: ", time.time() - startTime,  
		#print n
		#print reducedData
		
		if n != 0:
			startTime = time.time()
			
			result += papadimitriou(reducedData)
			print "Total Time", time.time() - startTime
		else:
			result += '0'

		
		
	
	print 'Result: ', result

if __name__ == "__main__":
	startTime = time.time()
	'''
	D = {}
	D[1] = True
	D[2] = False
	D[3] = True
	D[-1] = not D[1]
	D[-2] = not D[2]
	D[-3] = not D[3]

	print flipChoice(D, [1, 2])
	'''

	#reducedData = set([(-355438, -81794), (367886, 216948), (34142, 290996), (37170, -196347), (-174828, 364297), (390311, 41668), (-292521, -2776), (-160055, 282053), (-274615, 306344), (381467, 218710), (-218417, -371756), (-37724, 384722), (323143, 185754), (-347772, 366546), (173327, -365455), (-205269, -167795), (-359581, -177991), (155143, -185754), (359581, 183564), (276186, -347119), (-161943, -294252), (238337, -362454), (-35209, -155143), (237645, 80353), (-285577, 265033), (349571, -67666), (-316261, 108650), (68616, -251354), (-251460, -130275), (-260878, -233111), (237823, 210236), (258371, -387459), (320606, -375599), (-27396, -77013), (-54428, -256356), (40480, -335511), (-257373, 8808), (-91639, 316261), (294794, 375599), (218710, 365952), (-381464, 64406), (-112684, 91639), (-120100, 186640), (119784, -23548), (160855, -388377), (-379611, -39628), (-138057, -40480), (-233257, 130275), (-396608, 350242), (117877, 61349), (20028, 34747), (-246963, 313057), (18946, -369036), (-90039, 77380), (305340, 120100), (381780, 90039), (331606, -373701), (157310, -79717), (-68616, -374373), (355438, -320350), (381464, 187117), (-349096, -226126), (320732, -331606), (371756, 22844), (-356339, 64065), (134045, 122969), (-306344, -63766), (112684, 23548), (174225, -71604), (-385277, -319054), (-387672, -366546), (-166935, 319170), (-305340, -186282), (61944, -396896), (203294, 108127), (269876, -83087), (-356355, 19018), (-34835, 177419), (-320606, -208151), (-114688, 260878), (-373743, 107019), (-322598, -282053), (178324, 2776), (-273821, -231647), (-137231, 373131), (312480, -308525), (-34142, -354853), (-265788, 39628), (137231, -129941), (34835, -352718), (347119, 47342), (27396, -302345), (-242272, -330890), (255523, -254733), (-358900, 284947), (-294794, -20028), (-168450, 350762), (196347, 353262), (-88101, 366562), (-333997, 287707), (319968, 373743), (373701, 379611), (-366562, -278978), (-325443, -352257), (294461, 373726), (227905, 190788), (333515, -104818), (-237645, 123212), (88101, -320732), (28799, -165459), (-180046, 11020), (-112327, -325662), (-64065, 67666), (-391008, 356339), (6146, -277992), (-117877, -60918), (-23548, 276186), (117034, -107019), (325443, -160855), (-373131, 224522), (-313390, -34747), (256356, -110100), (-306396, 77013), (-22191, -6146), (7623, -230992), (390901, -30784), (-99562, 81794), (-77380, -119784), (271266, -61944), (-37170, -117034), (248604, -312480), (108098, -221033), (-122969, -160855), (362454, 120292), (-24682, 257373), (278978, -353262), (-350242, 292521), (-390311, 687), (133905, 36810), (83087, 365455), (-350762, 302345), (218417, -319968), (349890, -157221), (-128309, -36810), (177991, 277992), (308525, 359320), (97645, 71604), (67885, -265033), (79717, -289018), (-276186, 319054), (-16632, -394653), (352718, 35953), (358900, -295030), (-25674, 253752), (138057, 141931), (-174225, 387672), (99772, 166935), (266970, -64406), (168450, -67885), (-179611, 265306), (347772, 391008), (396896, -173100), (251354, 110100), (-210236, -687), (-11020, -14946), (-120292, 289018), (-202471, -61349), (191840, 64406), (-266002, -186640), (233257, -1714), (54428, -21064), (-351120, -12943), (12943, 253169), (128309, -232184), (-253752, 313390), (173100, -1230), (274615, 233111), (381467, -143615), (-374363, -366946), (353020, 35209), (157221, 270027), (-116278, 306396), (143615, -333515), (128764, -227905), (-22844, 265788), (-187117, -328420), (282918, 16632), (396608, -210012), (295030, 205269), (112327, -189327), (-265306, 151670), (-172477, 24669), (-41668, -173327), (21435, -270027), (-287707, -362508), (333997, 104818), (165459, -47342), (-294461, -283698), (-266970, -108650), (-269876, -133905), (-282918, -224522), (388377, -255523), (22191, -241669), (21064, -284947), (-130969, 387459), (283698, 340255), (318442, 246963), (25674, -374462), (-24669, -80386), (356339, 344325), (366946, -151670), (202471, 63766), (174828, 210012), (-205288, 242507), (-218710, -21435), (351120, 225036), (-153180, -340255), (354853, -364297), (40755, -242507), (352257, -367886), (226086, 385556), (-345839, -190788), (116278, -248604), (167795, -381780), (381119, -340255), (30784, -253398), (24682, 85738), (-237823, -313057), (320350, 180046), (-323143, 94048), (221033, -349890), (335511, -173100), (251460, 1714), (-134045, 160055), (36732, 250422), (-216948, 231647), (-319170, 374373), (-353020, 253398), (390993, -225036), (226126, 242272), (14946, 266002), (-101987, -349603), (161943, 270498), (349603, -68616), (375599, 130969), (-373726, 60918), (-85738, -108127), (369036, 189327), (273821, -46572), (138057, -203294), (46572, 99562), (-178324, -306344), (-381119, 232184), (-270498, -183564), (137527, 1230), (-157310, -227429), (-250422, 360782), (-79715, -137527), (321709, 208151), (-360782, -321709), (285577, 192355), (254733, 374363), (-35953, -238337), (-318442, 179611), (-384722, 114688), (-346531, 394653), (-8808, 186282), (356355, -365952), (-128764, -258371), (-108098, 225036), (-19018, 205288), (79715, 349096), (346531, -177419), (-290996, -271266), (-226086, -97645), (-36732, 330890), (-192355, -94048), (-141931, -390901), (232143, 153180), (-7623, -18946), (129941, -99772), (-191840, 172477), (-385556, 362508), (385277, -390993), (-381467, 294252), (230992, 80386), (101987, -40755), (374462, -349571), (-359320, -80353), (-344325, -28799), (-232143, 325662), (322598, 37724), (-253169, 241669), (328420, 345839), (227429, -123212)])

	#print papadimitriou(reducedData)

			
	runPS6()

	
	print "Total Time", time.time() - startTime



