handle = open('mbox-short.txt')
count = 0
for line in handle:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	count = count + 1
	arroba = line.find('@')
	espacio = line.find(' ', arroba)
	#a partir de arroba
	host = line[arroba+1 : espacio]
	if not host.find('edu'):
		continue
	print(count, '\n', host, '\n', line)