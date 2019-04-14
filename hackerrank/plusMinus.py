def plusMinus(arr):
    totCnt = 0
    lessThanZero = 0
    equalToZero = 0
    largerThanZero = 0

    for i in arr:
        totCnt += 1
        if i > 0:
            largerThanZero += 1
        elif i == 0:
            equalToZero += 1
        else:
            lessThanZero += 1

    print('{0:.6f}'.format(float(largerThanZero) / float(totCnt)))
    print('{0:.6f}'.format(float(lessThanZero) / float(totCnt)))
    print('{0:.6f}'.format(float(equalToZero) / totCnt))

a = [-4, 3, -9, 0, 4, 1]

#print a
plusMinus(a)