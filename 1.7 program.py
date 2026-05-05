a=float(input("enter a first side:"))
b=float(input("enter a second side:"))
c=float(input("enter a third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)**0.5)
print("the area of the triangle is: %0.3f"%area)
