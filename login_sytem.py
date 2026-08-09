def password_validator(password):
    if(len(password)<8):
        print("Password Must be 8 chracter long")
    is_digit=False
    upper=False
    lower=False
    for char in password:
        if char.isdigit():
            is_digit=True
        elif char.islower():
            lower=True
        elif char.isupper():
            upper= True
    if is_digit and upper and lower:
        print("Password saved")
        return True
    elif (is_digit==False):
        print("password must contain digit")
        return False
    elif (upper==False):
        print("Must contain upper chracter")
        return False
    elif (lower==False):
        print("must contain lower chracter ")
        return False

name  = input("Enter the name: ")
while(len(name)<1):
    name  = input("Enter the name: ")
password = input("Enter the password: ")
while (password_validator(password)==False):
    password = input("Enter the password: ")
login_username = input("Enter the username: ")
while(len(login_username)<1):
    login_username = input("Enter the username: ")
login_password= input("Enter the login Password: ")
while( login_password!=password):
    login_password = input("Enter the password Again: ")
print("You are succefully logged in. ")




