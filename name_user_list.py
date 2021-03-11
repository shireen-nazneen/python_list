List_names=["shireen","naz","kumar","sudha","jyoti","janwi"]
i=0
user_input=input("enetr any chr____")
while i<len(List_names):
    if List_names[i][0]==user_input:
        print(List_names[i])
    i=i+1