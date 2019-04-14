def timeConversion(s):
    #
    # Write your code here.
    #
    add = 0
    s = s.split(':')

    if "PM" in s[-1]:
    	if int(s[0]) == 12:
    		add = 0
    	else:

    		add = 12
    	s[-1] = s[-1].replace("PM", "")

    else:
    	s[-1] = s[-1].replace("AM", "")
    	if int(s[0]) == 12:
    		add = -12
    	

   
    s[0] = str(int(s[0]) + add).zfill(2)

    return ":".join(s)

s = "07:05:45PM"
output = "19:05:45"
result = timeConversion(s)
print result

s = "07:05:45AM"
output = "19:05:45"
result = timeConversion(s)
print result

s = "12:05:45AM"
output = "19:05:45"
result = timeConversion(s)
print result