def traverse_with_while(arr):
    i = 0
    while i < len(arr):
        print(arr[i], end = " ")
        i += 1

n = int(input("Enter the size of array:")).rstrip()

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element:")).rstrip()
    
traverse_with_while(arr)