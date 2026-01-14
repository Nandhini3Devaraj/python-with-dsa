n=int(input())
original=n
reversed=0
while n>0:
    digit=n%10
    reversed = reversed * 10 + digit
    print(digit)
    n=n//10
if reversed==original:
    print("palindrome")
else:
    print("not palindrome")    