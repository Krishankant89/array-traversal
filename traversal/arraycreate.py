n = int(input("Enter the size of array:"))

arr = [0] * n

for i in range(n):
    element = int(input("Enter element:"))
    arr[i] = element
    
print("Array elements are:")
for i in range(n):
    print(arr[i])