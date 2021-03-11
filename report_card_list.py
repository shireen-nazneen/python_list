marks=[[12,34,68,48,30],[24,56,46,50,24,38],[24,76,90,57,20,10,60]]
Sum=0
i=0
while i <len(marks):
    j=0
    while j<len(marks[i]):
        Sum=Sum+marks[i][j]
        j=j+1
    i=i+1
print(Sum)
    