n=int(input("enter the values:"))
arr=[]
for i in range(n):
    num=int(input("enter num:"))
    arr.append(num)
print("array:",arr)
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

a=int(input("enter the number of queries:"))




for _ in range(a):
    l,r=map(int,input("enter l and r:").split())
    

    if l==0:
        print("prefix sum:",prefix[r])
    else:
            print(prefix[r]-prefix[l-1])