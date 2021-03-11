n=30
num=[10, 11, 12, 13, 14, 17, 18, 19]
i=0
empty=[]
while i<len(num):
    j=i
    while j<len(num):
        if num[i]+num[j]==30:
            Sum=[num[i],num[j]]
            empty.append(Sum)
        j=j+1
    i=i+1
print(empty)        
        