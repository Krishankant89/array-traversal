def first_index_insertion(arr, n, val):
        
    #insert new value at first position
    arr[n] = val
    n += 1
    
    print("Updated array:", arr[:n])

n = int(input("Enter the size of array:"))    
# extra space needed
arr = [0] * (n + 1)

for i in range(n):
    arr[i] = int(input(f"Enter element {i}: "))

val = int(input("Enter value to insert at last position: "))

first_index_insertion(arr, n, val)