elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
c_1=0
sum_1=0
c_2=0
sum_2=0
while i<len(elements):
    if elements[i]%2==0:
        c_1+=1
        sum_1+=elements[i]
    else:
        c_2+=1
        sum_2+=elements[i]
    i=i+1
print(sum_1/c_1,"avrage of even number")
print(sum_2/c_2,"avrage of odd number")