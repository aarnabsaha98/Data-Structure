# T.C. = o(N)
def mergeSortedArray(arr1,arr2,k):
    q = 0
    p = 0
    d = 0
    # if len(arr1) < len(arr2):
    #     temp = [] * len(arr2)
    # temp = [] * len(arr1)
    m = len(arr1) 
    n = len(arr2)
    temp = [0] *(m+n) 
    while p < len(arr1) and q < len(arr2):
        if arr1[p] < arr2[q]  :
            temp[d] = (arr1[p])
            p += 1
            
        else :
            temp[d] = (arr2[q])
            q+=1
        d += 1
    while q < len(arr2):
        temp[d]  = (arr2[q])
        d+=1
        q += 1
    while p < len(arr1):
        temp[d] = arr1[p]
        d +=1
        p+=1
    #return temp
    return temp[k-1] if k < len(temp) else -1

arr1 = [2,3,6,7]
arr2 = [1, 4, 8, 10]
k = 3
print(mergeSortedArray(arr1,arr2,k))


# K-th Element of Two Sorted Arrays

# T.C = O(K)
def findelement(arr1,arr2 , k_req):
    i ,j ,k = 0 , 0 , 0
    
    # here we have a count that will keep track of kth element in arr1 and arr2 
    # if we got we return that 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j] :
            k +=1
            
            if k == k_req:
                return arr1[i] 
            
            i+=1
        else:
            k+=1
            
            if k == k_req:
                return arr2[j]
            j+=1
            
    while i < len(arr1):
        k+=1
        if k_req == k:
            return arr1[i]
        i+=1
        
    while j < len(arr2):
        k+=1
        if k == k_req:
            return arr2[j]
        j+=1
        
        