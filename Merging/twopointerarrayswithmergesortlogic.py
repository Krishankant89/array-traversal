def merged_array(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    n1 = len(arr1)
    n2 = len(arr2)
    
    
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
                merged.append(arr2[j])
                j += 1
            
    while i < n1:
        merged.append(arr1[i])
        i += 1
    while j < n2:
        merged.append(arr2[j])
        j += 1
        
    return merged

arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
result = merged_array(arr1, arr2)
print(result)