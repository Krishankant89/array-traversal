def traverse(arr, index):
    if index == len(arr): #base case
        return
    print(arr[index])
    traverse(arr, index + 1) #recursive case
    
n = int(input("Enter the size of array:"))

arr = [0] * n

for i in range(n):
    arr[i] = int(input(f"Enter the elements{i}:"))
    
traverse(arr,0)