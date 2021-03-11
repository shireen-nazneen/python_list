List_1=[1,2,3,4,5,6]
List_2=[2,3,1,0,6,7]
i=0
empty_list=[]
while i<len(List_1):
    if List_1[i] not in List_2:
        empty_list.append(List_1[i])    
    i=i+1
print(empty_list)