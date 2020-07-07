def insertionSort(arr): 
    p=int(input('enter 1 for ascending or 2 for desecnding: '))
    if p == 1:
        for i in range(1, inp):
             key = arr[i] 
             j = i-1
             while j >= 0 and key < arr[j] :
                  arr[j + 1] = arr[j] 
                  j -= 1
             arr[j + 1] = key
    elif p==2:
        for i in range(1, inp):
             key = arr[i] 
             j = i-1
             while j >= 0 and key > arr[j] : 
                 arr[j + 1] = arr[j] 
                 j -= 1
             arr[j + 1] = key 
    else:
        print("opps") 
                   
arr=[]
inp=int(input('ho many numberms in array: '))
for i in range(inp):
    p=int(input())
    arr.append(p) 
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i]) 
 