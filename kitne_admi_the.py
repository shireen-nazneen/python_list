elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
c_1=0
c_2=0
while i<len(elements):
    if elements[i]%2==0:
        c_1+=1
    else:
        c_2+=1
    i=i+1
print(c_2, "numbers are odd")
print(c_1,"numbers are even")
        