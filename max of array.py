a=int(input("enter the length of array:"))
arr=list()
for i in range(a):
    num=int(input("enter the element:"))
    arr.append(num)
maximum=max(arr)
print("array:",arr)
print("maximum",maximum)