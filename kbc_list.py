
question_list = [
    "How many continents are there?",              
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"    
]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = ["3", "4", "1"] 
lifeline_option=[["four","seven"],["channai","dellhi"],["softoware", "counseling"]]
lifeline_solution=["2","2","1"]


i=0
lifeline_count=0
while i<len(question_list):
    j=0
    index=1
    print(question_list[i])
    while j<len(options_list[i]):
        print(index,options_list[i][j])
        j=j+1
        index=index+1
    if index==5:
        user_input=input("enter your answer/ or use lifline")
        if user_input=="5050":
            if lifeline_count==0:
                l=0
                index2=1
                while l<len(lifeline_option[i]):
                    print(index2,lifeline_option[i][l])
                    l+=1
                    index2+=1
                    lifeline_count+=1
                user=input("enter your answer")
                if user==lifeline_solution[i]:
                    print("your answer is correct")
                else:
                    print("sadly your answer is wrong")
                    break
            else:
                print("you alrady use this lifline")
                user=input("enter your answer")
                if user==solution_list[i]:
                    print("your answer is correct")
                else:
                    print("sadly answer is wrong")
                    break
        elif user_input==solution_list[i]:
            print("your answer is correct")
        else:
            print("sadly answer is wrong")
            break
    i+=1

            
                
                                
        
    
            
