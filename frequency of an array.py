from optparse import Values
from sys import maxsize


l=int(input("enter the length:"))
arr=[]
frequency={}
for i in range(l):
    
    num=int(input("enter the num:"))
    arr.append(num)

for i in arr:
    if i in frequency:
        frequency[i]=frequency[i]+1
        
    else:
        frequency[i]=1
print("frequency:",frequency)

for key, value in frequency.items():
    max_freq=max(frequency.values())
    if value==max_freq:
        print("most freq values:",key)
    else:
        if value==1:
            print("non repeating values:",key)
            break
       
                   

