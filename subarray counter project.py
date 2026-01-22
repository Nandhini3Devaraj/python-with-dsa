n=int(input("enter the size of the array:"))
arr=[]
for i in range(n):
    num=int(input("enter the values:"))
    arr.append(num)
print("array:",arr)
subsum=[]
for i in range(n):
    for j in range(i,n):
        subarray=arr[i:j+1]
        sub_sum=sum(subarray)
        print("subarray:",subarray)
        print("subsum:",sub_sum)
        subsum.append(sub_sum)
print("max_subsums:",max(subsum))        
      


        



           

