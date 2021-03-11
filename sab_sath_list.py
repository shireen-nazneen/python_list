
elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum_odd=0
sum_even=0
sum_all=0
c1=0
c2=0
c3=0
while i<len(elements):
    sum_all+=elements[i]
    c1+=1
    if elements[i]%2==0:
        sum_even+=elements[i]
        c2+=1
    if elements[i]%2!=0:
        sum_odd+=elements[i]
        c3+=1
    i=i+1
print(sum_even/c2,"this is avarge of even",sum_even,c2)
print(sum_odd/c3,"this is avarge of odd ",sum_odd,c3)
print(sum_all/c1,"this is avrage of all",sum_all,c1)