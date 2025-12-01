def acc(x,y):
    email = x
    password = y
    valid = False
    val = False

    if "@" not in x: 
            print("You need to have an @ symbol")
            valid = False
    if "@" in x:
            print("Your Email is valid")
            valid = True

    if len(password) < 8:
            print("Your password must be at least 8 characters long")
    if not any(ch.isdigit() for ch in password):
           print("Your passsword must include at least one number")

    if not (ch.isuppper() for ch in password):
           print("Your password must include one uppercase letter") 

    if (len(password) > 8) and (ch.isdigit() for ch in password) and (ch.isupper() for ch in password):
             print("Your Password is valid")
             val = True

    if val == True and valid == True:
             print("Logged in Correctly")



acc("Jayden@415","v")
    