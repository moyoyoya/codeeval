#leer mas



import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	otro = []
	cosa = 0
	if test.strip() != '':
		if len(test) > 55:
			test = test[:40]
			if test[39] == ' ':
				test = test[:39]
			otro = test.split()
			if len(otro)>1:
				otro = otro[-1]
				cosa = len(test)-len(otro)-1
				test = test[:cosa] + '... <Read More>'
			else:
				test += '... <Read More>'
		else:
			test = test.strip()
		print(test)
	else: 
		None



test_cases.close()
