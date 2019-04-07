def maxCrossingSum(arr, l, m, h) : 

    l_index = 0 
    r_index = 0

    # Include elements on left of mid. 
    sm = 0; left_sum = -1000000
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) :
            l_index= i
            left_sum = sm 
        
    # Include elements on right of mid 
    sm = 0; right_sum = -1000000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 

        if (sm > right_sum) :
            r_index=i
            right_sum = sm 
            
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum, l_index, r_index
  
 
# Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h) : 
      
    # Base Case: Only one element 
    if (l == h) : 
        return arr[l], l, h
   
    # Find middle point 
    m = (l + h) // 2

    max_sum, l1, l2 = maxSubArraySum(arr, l, m)
    print(l1, l2)

    right_sum, r1, r2 = maxSubArraySum(arr, m+1, h)
    print("r", r1, r2)
    
    cross_sum, c1, c2 = maxCrossingSum(arr,l, m, h)
    print("c", c1, c2)

    if max_sum<right_sum:
        max_sum, l1,l2 = right_sum, r1, r2

    if max_sum<cross_sum:
        max_sum, l1,l2 = cross_sum, c1, c2

    return max_sum, l1, l2
              

arr = [2, 3, -4, 5, 7] 
n = len(arr) 
  
max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum)
