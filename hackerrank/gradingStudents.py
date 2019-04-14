# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.

# Sam is a professor at the university and likes to round each 
#student's  according to these rules:

# If the difference between the grade and the next multiple of 5  
# is less than 3, round  up to the next multiple of 5.
# If the value of  is less than 38, no rounding occurs as 
# the result will still be a failing grade.

def gradingStudents(grades):
    def gradeRounding(g):
    	if g < 38:
    		#no rounding
    		return g
    	elif g % 5 < 3:
    		#no rounding
    		return g
    	else:
    		#round up
    		return g + (5 - g % 5)

    for i in xrange(len(grades)):
    	grades[i] = gradeRounding(grades[i])
    
    return grades


g = [73, 67, 38, 33]
print gradingStudents(g) == [75, 67, 40, 33]