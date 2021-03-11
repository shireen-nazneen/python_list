num=int(input("enter number"))
List=[]
while num>0:
    rimainder=num%2
    List.append(rimainder)
    num=num//2
print(List)
i=0
decimal=0
while i<len(List):
    if List[i]==1:
        decimal+=2**i
    i=i+1
print(decimal)