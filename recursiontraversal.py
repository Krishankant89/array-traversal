def traverse(arr, index):
    if index == len(arr):
        return
    print(arr[index])
    traverse(arr, index + 1)
    
n = int(input("Enter the size of array:"))

arr = [0] * n

for i in range(n):
    arr[0] = int(input(f"Enter the elements{i}:"))
    
traverse(arr,0)