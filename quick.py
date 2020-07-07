def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]
    if x==1:     
        for j in range(low , high): 
            if   arr[j] < pivot:  
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 )
    elif x==2:
        for j in range(low , high):
            if   arr[j] > pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return (i+1)
    else:
        print("Iss umar hain karle galti se misatke beta")       
  
def quickSort(arr,low,high): 
    if low < high: 
   
        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
   
arr = []
inp=int(input("how many elements in array: "))
for i in range(inp):
    p=int(input())
    arr.append(p)
x=int(input("asecending order for press 1  or 2 for descendinf order: "))     
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
