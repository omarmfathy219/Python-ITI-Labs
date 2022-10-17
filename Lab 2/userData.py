# Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not.

def userData():
    while True:
        name = input("Please Enter your name: ")
        if (name != '' and not (name.isdigit())):
            break
    email = input("Please Enter your Email: ")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (regex.search(regex, email)):
        print(f"Your name is: {name} and your email is: {email}")
    else:
        print("Invalid Email")

userData()