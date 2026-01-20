n=int(input("array values:"))
arr=[]
for i in range(n):
    num=int(input("enter the valur:"))
    arr.append(num)
print("array:",arr)
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
l=int(input("enter l:")) 
r=int(input("enter r:"))
if l==0:
    print("prefix sum:",prefix[r])
else:
    print("prefix sum:",prefix[r]-prefix[l-1])           