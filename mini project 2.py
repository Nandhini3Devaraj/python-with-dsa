#subarray analyzer.py
#prefix sum and range querry
n=int(input("enter the no of elements in array:"))
arr=[]
for i in range(n):
    num=int(input("enter the num:"))
    arr.append(num)
print("array:",arr)
prefix=[0]*(len(arr))
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("prefix:",prefix)

#max difference


max_diff=arr[1]-arr[0]
a=arr[0]
b=arr[1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        diff=arr[j]-arr[i]
        if max_diff<diff:
            max_diff=diff
            a=arr[j]
            b=arr[i]
print(f"maximum difference:{max_diff} ({b}-{a})")


#equilibrium indices 13522 
total_sum=sum(arr)


left_sum=0
found=False
for i in range(n):
    right_sum=total_sum-left_sum-arr[i]  
    if left_sum==right_sum:
        print("equilibrium index is:",i)
        break
    left_sum=left_sum+arr[i]
else:
    print("it has no equilibrium")      


   