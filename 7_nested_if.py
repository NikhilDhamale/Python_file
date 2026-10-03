username=input("enter the username : ")
password=input("enter the password :")

if (username=="admin" and password=="pass"):
    print("login success")

else:
    if(username !="admin"):
        print("enter correct username ")
    else:
        print("wrong password")
