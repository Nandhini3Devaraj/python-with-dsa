


a=int(input("enter the length of array:"))
arr=list()
for i in range(a):
    num=int(input("enter a number:"))
    arr.append(num)
total=sum(arr)
minimum=min(arr)
maximum=max(arr)
print('array:',arr)
print("sum:",total)
print("minimum:",minimum)
print("maximum:",maximum)
count_even=0
count_odd=0
for i in arr:
 if i%2==0:
    count_even=count_even+1
   
 else: 
    count_odd=count_odd+1   
print("odd:",count_odd)
print("even:",count_even)
frequency={}
for i in arr:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1 
print("frequency of array:",frequency)           


    


