def acc(x,y):
    email = x
    password = y
    valid = False
    char = 0

    if "@" not in x: 
            print ("You need to have an @ symbol")
    if "@" in x:
            valid = True

    if valid == True:
        print("What is the password?")

    for i in y:
       char = char + 1
    if char < 8:
            print("Your password must be at least 8 characters long")
    if str.isdigit(y) 


      
acc("Jayden415")    
    