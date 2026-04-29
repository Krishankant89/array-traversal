def mergearrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    
    merged = [0] * (n + m)
   #copy elements from arr1 and arr2 into merged array 
    for i in range(n):
        merged[i] = arr1[i]
    for j in range(m):
        merged[n +j] = arr2[j]
        #i use [n+j] cause first 'n' positions area already taken by 'arr1' so 'arr2' should start right after that
    merged.sort()
    
    
    for i in range(n):
        arr1[i] = merged[i]
        '''
        if we use [n+i] that means skip first elements, start from next part
        '''
        
    for j in range(m):
        arr2[j] = merged[n + j]
        
if __name__ == "__main__":
    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]
    
    mergearrays(arr1, arr2)
    
    print(*arr1)
    print(*arr2)