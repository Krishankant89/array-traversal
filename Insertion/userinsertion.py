def user_insertion(arr,n, index, val):
    if 0 <= index <= n:
        
        for i in range(n, index, -1):
            arr[i] = arr[i-1]
            
        
        arr[index] = val
        n += 1
        
        print("updated array:", arr[:n])
    else:
        print("Invalid index")

n = int(input("Enter the size of array:"))

arr = [0] * (n+1)

for i in range(n):
    arr[i] = int(input(f"Enter the elements {i}:"))
    
index = int(input("Enter the index value to insert:"))
val = int(input("Enter value to insert:"))
    
user_insertion(arr, n, index, val)