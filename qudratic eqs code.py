a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c = int(input("Enter value of c :"))

d = (b*b) - (4*a*c)

if(d>0):
    print("Real and different roots")
    print((-b + d**0.5)/(2*a))
    print((-b - d**0.5)/(2*a))
    
elif(d<0):
    print("Real and same roots")
    print(-b / (2*a))
    
elif((d==0)):
    print("Quadratic equation has equal roots")
    print(-b/(2*a))