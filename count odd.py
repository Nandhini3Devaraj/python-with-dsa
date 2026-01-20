a=int(input("enter the length:"))
arr=list()
for i in range(a):
    num=(int(input("enter the number:")))
    if num%2 != 0:
        arr.append(num)
print("no of odd:",len(arr))        

