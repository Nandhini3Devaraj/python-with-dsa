count_x=0
count_y=0
arr=int(input("enter the elements:"))
list=[]
dictionary={}
x=int(input("x;"))
y=int(input("y:"))
for i in range(arr):
    num=int(input("enter the element:"))
    list.append(num)
for i in list:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1
print("items:",dictionary)        
for key,values in dictionary.items():
    if key>x:
        count_x=count_x+1
    if key<y:
            count_y=count_y+1
print("greater than x:",count_x)
print("lesser than y:",count_y)
count_xy=0
for key,values in dictionary.items():
    if key>x and key<y:
        count_xy+=1
print("numbers greater than x and leass than10 y:",count_xy)                                   

