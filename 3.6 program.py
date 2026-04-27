n=int(input("enter the value of n i"))
mylist=[]
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
    print("even numbers are")
    print("[",end=" ")
    for num in mylist:
        if num%2==0:
            print(num,end=" ,")
            print("]")
