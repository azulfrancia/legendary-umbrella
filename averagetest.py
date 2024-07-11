count = 0
sum = 0
print('before',count,sum)
for value in [5,4,3,2,1]:
	count = count+1
	sum = sum + value
	print(count,sum,value)
average=int(sum / count)
print('after',count,sum,average)