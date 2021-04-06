def login(userid, password):
    if(userid == "pranavkr97" and password == "dobaramatpuchna"):
        return True
    else:
        return False  

userid = input("userid: ")
password = input("password: ")

print(login(userid, password))