a=["shireen",2,4.0,]
i=0
empty=[]
while i<len(a):
    if (type(a[i]))==int:
        c=a[i]
        b=c**2
        empty.append(b) 
    elif (type(a[i]))==str:
        empty.append("str")
    else:
        empty.append("float")
    i=i+1
print(empty)
    