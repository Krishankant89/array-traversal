def mergearrays(arr1, arr2):
    n = int(input("enter the size of array:"))
    m = int(input("Enter the size of array;"))
    
    
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
    arr1 = int(input("Enter the elements:"))
    arr2 = int(input("Enter the elements:"))
    
    mergearrays(arr1, arr2)
    
    print(*arr1)
    print(*arr2)