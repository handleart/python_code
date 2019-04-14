import math
import random
from time import time
from itertools import chain
from collections import defaultdict

def papa(clause_pairs):
    """
    Papadimitriou's 2SAT algorithm using the principle of local search.
    
    Pick a random assignment of the variables and test the satisfiability,
    if satisfied return satisfiable, otherwise randomly choose a failed
    clause and randomly choose one of its two variable and flip its value.
    """
    variables = set(map(abs, chain(*clause_pairs)))
    num_of_repeat = int(math.log(len(variables), 2))
    for i in range(num_of_repeat):
        assign = {}
        for var in variables:
            assign[var] = random.choice([True, False])
            assign[-var] = not assign[var]
        for j in range(2 * pow(len(variables), 2)):
            false_clause_pairs = pick_false_clause(clause_pairs, assign)
            if false_clause_pairs == []:
                return 1
            else:
                chosen_clause = random.choice(false_clause_pairs)
                chosen_var = abs(random.choice(chosen_clause))
                assign[chosen_var] = not assign[chosen_var]
                assign[-chosen_var] = not assign[chosen_var]
    return 0


def pick_false_clause(clause_pairs, assign):
    """Given the assignment of each variable, return a list of the clauses
    that are not satisfied. Empty list means 2SAT is satisfied.
    'clause_pairs' in form of set((variable1, variable2), ...)
    'assign' in form of {variable: boolean, ...}."""

    return [x for x in clause_pairs if not (assign[x[0]] | assign[x[1]])]

def reduce_clause(all_clause_pairs):
    """Given all the clauses of a 2SAT problem, remove the clauses that include
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
    
    'var_clause_dict' in forms of {variable:set(clause, ...), ...} shows all
    clauses containing that variable for each variable, a clause in an entry
    gets removed if either of its variables is singular.
    
    'clause_var_dict' in forms of {clause:[variable, variable], ...} shows the
    two variables involved in that clause for each clause, an entry gets removed
    if either of its variables is singular.
    
    Reduction in 'var_clause_dict' and 'clause_var_dict' MUST be in sync. After
    each reduction iteration, the values of 'clause_var_dict' are the remaining
    variables and the keys of 'var_clause_dict' are the remaining clauses.
    https://class.coursera.org/algo2-002/forum/thread?thread_id=431#post-1601
    """

    singular_var = set()
    clause_var_dict = {} 
    var_clause_dict = defaultdict(set)
    for x, y in all_clause_pairs:
        var_clause_dict[x].add((x, y))
        var_clause_dict[y].add((x, y))
        clause_var_dict[(x,y)] = [x, y]
    while True:
        for var in singular_var:
            for clause in var_clause_dict[var].copy():
                del clause_var_dict[clause]
                var_clause_dict[clause[0]] -= set([clause])
                var_clause_dict[clause[1]] -= set([clause])
        reduced_var = set(chain(*clause_var_dict.values()))
        singular_var = set([i for i in reduced_var if -i not in reduced_var])
        if singular_var == set():
            break
    return set(clause_var_dict.keys())
 

def main():
    out = []
    for i in range(1, 7):
        all_clause_pairs = set()
        with open('data/2sat%s.txt' % i) as file_in:
        #with open('test.txt') as file_in:
            next(file_in)
            for line in file_in:
                x, y = map(int, line.strip().split(' '))
                all_clause_pairs.add((x, y))
        startTime = time()
        reduced_clause_pairs = reduce_clause(all_clause_pairs)
        print "Time to Read File", time() - startTime, 
        #print len(reduced_clause_pairs), len(set(chain(*reduced_clause_pairs)))
        #print reduced_clause_pairs
        startTime = time()

        #reduced_clause_pairs =set([(-355438, -81794), (367886, 216948), (34142, 290996), (37170, -196347), (-174828, 364297), (390311, 41668), (-292521, -2776), (-160055, 282053), (-274615, 306344), (381467, 218710), (-218417, -371756), (-37724, 384722), (323143, 185754), (-347772, 366546), (173327, -365455), (-205269, -167795), (-359581, -177991), (155143, -185754), (359581, 183564), (276186, -347119), (-161943, -294252), (238337, -362454), (-35209, -155143), (237645, 80353), (-285577, 265033), (349571, -67666), (-316261, 108650), (68616, -251354), (-251460, -130275), (-260878, -233111), (237823, 210236), (258371, -387459), (320606, -375599), (-27396, -77013), (-54428, -256356), (40480, -335511), (-257373, 8808), (-91639, 316261), (294794, 375599), (218710, 365952), (-381464, 64406), (-112684, 91639), (-120100, 186640), (119784, -23548), (160855, -388377), (-379611, -39628), (-138057, -40480), (-233257, 130275), (-396608, 350242), (117877, 61349), (20028, 34747), (-246963, 313057), (18946, -369036), (-90039, 77380), (305340, 120100), (381780, 90039), (331606, -373701), (157310, -79717), (-68616, -374373), (355438, -320350), (381464, 187117), (-349096, -226126), (320732, -331606), (371756, 22844), (-356339, 64065), (134045, 122969), (-306344, -63766), (112684, 23548), (174225, -71604), (-385277, -319054), (-387672, -366546), (-166935, 319170), (-305340, -186282), (61944, -396896), (203294, 108127), (269876, -83087), (-356355, 19018), (-34835, 177419), (-320606, -208151), (-114688, 260878), (-373743, 107019), (-322598, -282053), (178324, 2776), (-273821, -231647), (-137231, 373131), (312480, -308525), (-34142, -354853), (-265788, 39628), (137231, -129941), (34835, -352718), (347119, 47342), (27396, -302345), (-242272, -330890), (255523, -254733), (-358900, 284947), (-294794, -20028), (-168450, 350762), (196347, 353262), (-88101, 366562), (-333997, 287707), (319968, 373743), (373701, 379611), (-366562, -278978), (-325443, -352257), (294461, 373726), (227905, 190788), (333515, -104818), (-237645, 123212), (88101, -320732), (28799, -165459), (-180046, 11020), (-112327, -325662), (-64065, 67666), (-391008, 356339), (6146, -277992), (-117877, -60918), (-23548, 276186), (117034, -107019), (325443, -160855), (-373131, 224522), (-313390, -34747), (256356, -110100), (-306396, 77013), (-22191, -6146), (7623, -230992), (390901, -30784), (-99562, 81794), (-77380, -119784), (271266, -61944), (-37170, -117034), (248604, -312480), (108098, -221033), (-122969, -160855), (362454, 120292), (-24682, 257373), (278978, -353262), (-350242, 292521), (-390311, 687), (133905, 36810), (83087, 365455), (-350762, 302345), (218417, -319968), (349890, -157221), (-128309, -36810), (177991, 277992), (308525, 359320), (97645, 71604), (67885, -265033), (79717, -289018), (-276186, 319054), (-16632, -394653), (352718, 35953), (358900, -295030), (-25674, 253752), (138057, 141931), (-174225, 387672), (99772, 166935), (266970, -64406), (168450, -67885), (-179611, 265306), (347772, 391008), (396896, -173100), (251354, 110100), (-210236, -687), (-11020, -14946), (-120292, 289018), (-202471, -61349), (191840, 64406), (-266002, -186640), (233257, -1714), (54428, -21064), (-351120, -12943), (12943, 253169), (128309, -232184), (-253752, 313390), (173100, -1230), (274615, 233111), (381467, -143615), (-374363, -366946), (353020, 35209), (157221, 270027), (-116278, 306396), (143615, -333515), (128764, -227905), (-22844, 265788), (-187117, -328420), (282918, 16632), (396608, -210012), (295030, 205269), (112327, -189327), (-265306, 151670), (-172477, 24669), (-41668, -173327), (21435, -270027), (-287707, -362508), (333997, 104818), (165459, -47342), (-294461, -283698), (-266970, -108650), (-269876, -133905), (-282918, -224522), (388377, -255523), (22191, -241669), (21064, -284947), (-130969, 387459), (283698, 340255), (318442, 246963), (25674, -374462), (-24669, -80386), (356339, 344325), (366946, -151670), (202471, 63766), (174828, 210012), (-205288, 242507), (-218710, -21435), (351120, 225036), (-153180, -340255), (354853, -364297), (40755, -242507), (352257, -367886), (226086, 385556), (-345839, -190788), (116278, -248604), (167795, -381780), (381119, -340255), (30784, -253398), (24682, 85738), (-237823, -313057), (320350, 180046), (-323143, 94048), (221033, -349890), (335511, -173100), (251460, 1714), (-134045, 160055), (36732, 250422), (-216948, 231647), (-319170, 374373), (-353020, 253398), (390993, -225036), (226126, 242272), (14946, 266002), (-101987, -349603), (161943, 270498), (349603, -68616), (375599, 130969), (-373726, 60918), (-85738, -108127), (369036, 189327), (273821, -46572), (138057, -203294), (46572, 99562), (-178324, -306344), (-381119, 232184), (-270498, -183564), (137527, 1230), (-157310, -227429), (-250422, 360782), (-79715, -137527), (321709, 208151), (-360782, -321709), (285577, 192355), (254733, 374363), (-35953, -238337), (-318442, 179611), (-384722, 114688), (-346531, 394653), (-8808, 186282), (356355, -365952), (-128764, -258371), (-108098, 225036), (-19018, 205288), (79715, 349096), (346531, -177419), (-290996, -271266), (-226086, -97645), (-36732, 330890), (-192355, -94048), (-141931, -390901), (232143, 153180), (-7623, -18946), (129941, -99772), (-191840, 172477), (-385556, 362508), (385277, -390993), (-381467, 294252), (230992, 80386), (101987, -40755), (374462, -349571), (-359320, -80353), (-344325, -28799), (-232143, 325662), (322598, 37724), (-253169, 241669), (328420, 345839), (227429, -123212)])

        out.append(papa(reduced_clause_pairs))
        print "Total Time", time() - startTime 
        
        #break 
    return out


if __name__ == "__main__":
    start = time()
    print main()
    print time() - start