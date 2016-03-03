"""Sample code to read in test cases:"""

import sys
import re
test_cases = open(sys.argv[1], 'r+')
for test in test_cases:
	if test.strip() != '':
		lista = test.split()
		auxiliar = []
		for i in lista:
			auxiliar.append(i.split(':')[0]+ i.split(':')[1] + i.split(':')[2])
			print(auxiliar)
		#if otra[0]> otra[1] and otra[0] > otra[2]:
		#	resultado += otra[0]
		#elif otra[1] 

		#print(otra)

test_cases.close()

