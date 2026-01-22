n=int(input("enter the no of elements in array:"))
arr=[]
for i in range(n):
    num=int(input("enter the elements:"))
    arr.append(num)
print("array:",arr)    
total_sum=sum(arr)
left_sum=0



for i in range(n):
    right_sum=total_sum-left_sum-arr[i]  
    if left_sum==right_sum:
        print("equilibrium index is:",i)
        break
    left_sum=left_sum+arr[i]
else:
    print("it has no equilibrium")

       