def first_index_insertion(arr, n, val):
    #shift all elments to one step to the right
    for i in range(n, 0, -1):
        arr[i] = arr[i -1]
        
    #insert new value at first position
    arr[0] = val
    n += 1
    
    print("Updated array:", arr[:n])

n = int(input("Enter the size of array:"))    
# extra space needed
arr = [0] * (n + 1)

for i in range(n):
    arr[i] = int(input(f"Enter element {i}: "))

val = int(input("Enter value to insert at first position: "))

first_index_insertion(arr, n, val)