numlist = list()
while True:
	inp = input('nro: ')
	if inp == 'listo':
		break
	try:
		try:
			if not inp == inp.find('.'):
				value1 = int(inp)
				numlist.append(value1)
				print('su nro fue',value1)
		except:
			if 
			elif inp == inp.find('.'):
				value2 = float(inp)
				numlist.append(value2)
				print('su nro fue:',value2)
	except:
		print('por favor, nro')
try:
	average = sum(numlist)/len(numlist)
	print('promedio:', average)
	print(numlist)
except:
	print('tocá pa ya, bobo')