s_username="EMC"
s_password="123"

uname=input("enter uname:")
password=input("enter password:")

def validaion():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False

print(validaion())
