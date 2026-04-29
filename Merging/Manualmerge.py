n1 = int(input("Enter size of array:"))
arr1 = [int(input(f"enter element {i+1}:")) for i in range(n1)]

n2 = int(input("enter size of array:"))
arr2 = [int(input(f'enter element {j+1}:')) for j in range(n2)]

merged = [0] * (n1 + n2)

for i in range(n1):
    merged[i] = arr1[i]

for j in range(n2):
    merged[n1 + j] = arr2[j]
    
print("Merged array:", merged)