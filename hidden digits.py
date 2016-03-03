import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	resul = ''
	for letra in test:
		dic = {'a': '0', 'b': '1', 'c': '2', 'd': '3','e': '4', 
		'f': '5','g':'6','h':'7','i':'8','j':'9'}
		if letra in dic:
			resul += dic[letra]
		else:
			try:
				resul += str(int(letra))
			except:
				None
	if resul == '':
		print('NONE')
	else:
		print(resul)

test_cases.close()