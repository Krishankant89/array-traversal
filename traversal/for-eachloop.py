def for_each_loop(arr):
    for element in arr:
        print(element, end = " ")

n = int(input("Enter the size of array:"))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter the elements:"))

for_each_loop(arr)