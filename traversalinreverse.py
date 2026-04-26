def reverse_traversal(arr):
    for i in range(len(arr) -1, -1, -1):
        print(arr[i])
        
n = int(input("Enter the size of array:"))

arr = [0] * n

for i in range(n):
    arr[i] = int(input(f"Enter the elements {i}:"))
    
reverse_traversal(arr)