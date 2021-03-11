magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
num=15
c=magic_square
i=0
Sum_right_Diagonals=0
Sum_left_Diagonals=0
if len(c[i])<=3:

    while i<len(c):
        j=0
        while j<=2:
            if i==j:
                Sum_right_Diagonals+=c[i][j]
            if i==0 and j==2 or i==1 and j==1 or i==2 and j==0:
                Sum_left_Diagonals+=c[i][j]
            j=j+1
        i=i+1
    if num==Sum_right_Diagonals and num==Sum_left_Diagonals:
         a=(True)
    else:
        a=(False)
    i=0
    Sum_raw1=0
    Sum_raw2=0
    Sum_raw3=0
    while i<len(c):
            j=0
            while j<=2:
                if i==0:
                    Sum_raw1+=c[i][j]
                elif i==1:
                    Sum_raw2+=c[i][j]
                else:
                    Sum_raw3+=c[i][j]
                j=j+1
            i=i+1
    if Sum_raw1==num and Sum_raw2==num and Sum_raw3==num:
        b=(True)
    else:
        b=(False)
    i=0
    Sum_c_1=0
    Sum_c_2=0
    Sum_c_3=0
    while i<len(c):
        j=0
        while j<len(c[i]):
            if j==0:
                Sum_c_1+=c[i][j]
            elif j==1:
                Sum_c_2+=c[i][j]
            else:
                Sum_c_3+=c[i][j]
            j=j+1
        i=i+1
    if Sum_c_1==num and Sum_c_2==num and Sum_c_3==num:
        c_1=(True)
    else:
        c_1=(False)
    if b and a and c_1==True:
        print(True,"this is a magic square")
    else:
        print(False,"this is a not magic square")
else:
    print(False, "this is not a magic squre")

        
        
    

    
