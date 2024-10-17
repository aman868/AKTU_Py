r = int(input("Enter the number of row: "))
c = int(input("Enter the number of columns: "))

M = []

print("Enter the elements row-wise:")

for i in range(r):
    row = []  
    for j in range(c):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)  
    M.append(row)  

print("\nMatrix:")
for row in M:
    print(row)

element_sum = 0
for i in range(r):
    for j in range(c):
        element_sum += M[i][j]

print(f"\nThe sum of all matrix elements is: {element_sum}")

for i in range(r):
    for j in range(c):
        element -= M[i][j]
        
print(f"\nThe subtraction of all matrix elements is: {element} \n")