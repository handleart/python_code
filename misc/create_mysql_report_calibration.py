#!/usr/bin/python
'''
Written by: Ardeshir Mostofi
Purpose of this script is to take a list of IDs and query them in the db at a rate of n at at time. 

inputFileName is the input filename (assumes one column, \n separated)
outputfileName is the output file name
sqlCredentialFile is the location of the information for authenticating with SQL server. This is not statically stored here for security reasons. 
case is the function that generates the various case statements for the query based on a field input name
query is the function that generates the query based on a list of contracts
numberOfRowsQueriedAtOnce is the number of IDs to search at the same time (to improve performance)


For change to the report, look at the createReport function


'''

import MySQLdb
import sys

#inputFileName = '/PG&E/20160627/ETOU_BPP_100k_SAIDs.txt'

print sys.argv

inputFileName = '/PG&E/20160809/TestFile.txt'
outputFileName = '/PG&E/20160809/output.txt'
sqlCredentialFile = '/Users/art/.sql/cred.txt'
delimiter = "\t"
numberOfRowsQueriedAtOnce = 10000

def case(val):
	case1 = ('	when ' + val + ' = "1" then "E1" '
			'	when ' + val + ' = "32" then "EVA" '
			'	when ' + val + ' = "47" then "E6" '
			'	when ' + val + ' = "238" then "ETOUA" '
			'   when ' + val + ' = "276" then "ETOUB" '
			'	else "" ')

	return case1;


def query(list_of_contracts):

	q = ("SELECT      entity_id AS 'Account ID',     contract_id AS 'Service Agreement ID',     servicepoint_id AS 'Service Point ID',     bill_start_date AS 'Bill Start Date',     bill_end_date AS 'Bill End Date',     ROUND(bill_total, 2) AS 'GridX Bill Charge',     ROUND(utility_bill_total, 2) AS 'PGE Bill Charge',     ROUND(utility_bill_total - bill_total, 2) AS 'Bill Gap Amount',     ROUND((utility_bill_total - bill_total) / utility_bill_total,             2) AS 'Bill Gap %',     IF(additional_field_2 = 1,         'Matched',         'Unmatched') AS 'Has Gap?',     utility_bill_usage 'PGE Usage',     billing_cycle_usage AS 'GridX Usage',     utility_bill_usage - billing_cycle_usage AS 'Usage Gap',     contract_name AS 'Rate Code',     additional_field_1 AS 'Gap Reason' FROM     pge.accountbillinglog WHERE     bill_start_date >= '2015-01-01'         AND batchid IN ('ping_calibration_0804_120k' , 'ping_calibration_0804_600k')         AND creation_date > '2016-08-07'         AND bill_id limit 1")
	
	return q


def loadData(f):
	return [i.strip('\r') for i in open(f, 'r').read().split('\n')][1:]

def loadCredentials(sqlCredentialFile):
	d = {}
	with open(sqlCredentialFile) as ff:
		for line in ff:
			(key, val) = line.split()
			d[key] = val

	return d

def createReport(inputFileName, outputfileName, sqlCredentialFile, delimiter, n):
	credentials = loadCredentials(sqlCredentialFile)
	db = MySQLdb.connect(host = credentials['host'],
						 user=credentials['user'],
						 passwd=credentials['passwd'],
						 db = credentials['db'])

	# Set up initial variables
	header = ['Account_ID', 'SA_ID', 'SP_ID', 'Bill_Options', 'Bill_Start_Date', 'Bill_End_Date', 'Rate1', 'Amt1', 'Rate2', 'Amt2', 'Rate3', 'Amt3', 'Rate4', 'Amt4']
	outputFile = open(outputFileName, 'w')
	outputFile.write(delimiter.join(header) + '\n')
	cur = db.cursor()

	data = loadData(inputFileName)
	i_start = 0
	i_end = n

	#run query and to write to file
	while True:
		#generate data set
		if len(data) < i_end:
			tmp = data[i_start:]
		else:
			tmp = data[i_start:i_end]
		
		print "Querying and writing rows", i_start, 'to', i_end

		#generate query
		q = query(tmp)
		#print q

		cur.execute(q);

		#write to file
		for i in cur:
			#print i
			A = []
			for x in i:
				try: 
					float(x)
					A.append("%0.2f" % x)
				except:
					A.append(str(x))

			aStr = delimiter.join(A)

			outputFile.write(aStr + '\n')

		if len(data) < i_end:
			break

		i_start = i_start + n
		i_end = i_end + n 

	db.close()

	
def testReport(inputFileName, outputfileName, delimiter):
	#data = '/PG&E/20160627/output.txt'

	result = set()
	resultDict = {}

	with open(outputfileName, 'r') as f:
		next(f)
		for line in f:
			val = line.strip('\n').split(delimiter)[1]
			result.add(val)

			if val not in resultDict:
				resultDict[val] = 1
			else:
				resultDict[val] += 1


	#data2 = '/PG&E/20160627/ETOU_BPP_100k_SAIDs.txt'
	originalSet = set()

	with open(inputFileName, 'r') as f:
		next(f)
		for line in f:
			originalSet.add(line.strip('\r\n'))

	tmp = originalSet - result
	print "Number of IDs in original query not in final report", len(tmp)

	if len(tmp) < 20:
		print tmp

	print "IDs with unexpected count of values returned "
	for i in resultDict:
		if resultDict[i] > 13 or resultDict[i] < 12:
			print i, resultDict[i]


if __name__ == '__main__':
	createReport(inputFileName, outputFileName, sqlCredentialFile, delimiter, numberOfRowsQueriedAtOnce)
	testReport(inputFileName, outputFileName, delimiter)
