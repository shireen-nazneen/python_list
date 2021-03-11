List_num=[2,3,6,4,1,5,9,8]
i=0
while i<len(List_num):
    j=0
    while j<len(List_num)-1:
        if List_num[j]>List_num[i]:
            List_num[j],List_num[i]=List_num[i],List_num[j]
        j+=1
    i+=1
print(List_num)
