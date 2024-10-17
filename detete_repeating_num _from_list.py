l = []

n = int(input("Enter number of elements : "))


for i in range(0, n):
    m = int(input())
    l.append(m)

    
u = list(set(l))
print("Updated list is this : ", u)  


r = [num for num in u if l.count(num) > 1]
print("Repeated numbers:", r)