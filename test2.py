while True:
	line = input('> ')
	if line[0] == '#': #es decir, si tiene
		continue #"#" como primer caracter [0]
	if line == 'chau':
		break
	print(line)
print('chau!')