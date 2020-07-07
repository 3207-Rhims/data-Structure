def selection(A):
    x=int(input(''' ------menu-----
            press 1 for ascending
            press 2 for decending: '''))
    if x==1:
        for i in range(len(A)):
            min_idx = i 
            for j in range(i+1, len(A)): 
                if A[min_idx] > A[j]: 
                    min_idx = j
                    A[i], A[min_idx] = A[min_idx], A[i]
    elif x==2:                            
        for i in range(len(A)):   
            min_idx = i 
            for j in range(i+1, len(A)): 
                if A[min_idx] < A[j]: 
                    min_idx = j
                    A[i], A[min_idx] = A[min_idx], A[i]
    else:
        print("opppppppppppps")
        
    for i in range(len(A)):
        print("%d" %A[i]) 

                
                        
inp=int(input("how many elements in array: "))
A=[]
for i in range(0,inp):
    p=int(input())
    A.append(p)

selection(A) 
