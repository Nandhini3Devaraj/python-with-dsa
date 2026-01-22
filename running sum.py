n=int(input("enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter the number:"))
    arr.append(num)
print("array:",arr) 
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

print("running sum:",prefix)    
