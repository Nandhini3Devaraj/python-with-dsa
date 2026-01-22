n=int(input("enter the no of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter the array element:"))
    arr.append(num)
max_diff=arr[1]-arr[0] 
a=arr[0]
b=arr[1]   
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        diff=arr[j]-arr[i]
        if  max_diff<diff:
          max_diff=diff
          a=arr[i]
          b=arr[j]
print(f"output:{max_diff} ({b}-{a})")
