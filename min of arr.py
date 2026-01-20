a=int(input("enter the length of array:"))
arr=list()
for i in range(a):
    num=int(input("enter the element:"))
    arr.append(num)
minimum=min(arr)
print("array:",arr)
print("minimum",minimum)    


