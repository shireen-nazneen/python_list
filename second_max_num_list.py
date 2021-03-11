list=[1,2,3,6,7,]
i=0
maxnum=0
scendmax=0
while i<len(list):
	if list[i]>maxnum:
		scendmax=maxnum
		maxnum=list[i]
		if scendmax<list[i] and maxnum>list[i]:
			maxnum=list[i]
	i=i+1
print(scendmax)