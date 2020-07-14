def binary_search(list, low, high, x): 
   
    if high >= low: 
  
        mid = (high + low) // 2
  
        if list[mid] == x: 
            return mid 
  
        elif list[mid] > x: 
            high=mid - 1
            return binary_search(list, low,high, x) 
        else: 
            low = mid + 1
            return binary_search(list,low, high, x) 
  
    else:  
        return -1
  
list = [ 2, 3, 4, 10, 40,45,47,48 ] 
x = 10
   
result = binary_search(list, 0, len(list)-1,x) 
print(result)               