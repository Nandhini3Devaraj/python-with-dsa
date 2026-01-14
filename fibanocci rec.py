a=int(input())
\

def fib(a):
    
        
        if a==1:
             return 1
        elif a==0:
            return 0      
        else:
            return fib(a-1)+fib(a-2)
for i in range (a):    
        print(fib(i),end=",")        


