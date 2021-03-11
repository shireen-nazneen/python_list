List=[34,50,100,4, 5, 6, 7,]
i=0
L=List[0]
while i<len(List):
    if List[i]<L:
        L=List[i]
    i=i+1
print(L)