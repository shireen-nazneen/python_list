n=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
i=0
empty=[]
while i<len(n):
    j=0
    c=0
    while j<len(n):
        if n[i]==n[j]:
            c+=1
        j=j+1
    if n[i] not in(empty) and c>0:
        empty.append(n[i])
    i=i+1
print(empty)