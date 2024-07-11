total = 0
count = 0
while True:
	inp = input('nro: ')
	if inp == 'listo':
		break
	try:
		value = float(inp)	
		total = total + value
		count = count + 1
	except:
		print('por favor, nro')
try:
	average = total/count
	print('promedio:', average)
except:
	print('tocá pa ya, bobo')