import re
import time
from MianPage import mainPage


def entryInputValidation():
    x = input("Enter Your Choice: ")
    if (x.isdigit() and int(x) in [1, 2]):
        return int(x)
    return entryInputValidation()

# <======================= Check Name Validation =======================>


def enterFName():
    x = input("Enter your First Name: ")
    if (x.isalpha() or not x):
        return x
    else:
        return enterFName()


def enterSName():
    x = input("Enter your second Name: ")
    if (x.isalpha() or not x):
        return x
    else:
        return enterSName()

# <======================= Email Validation =======================>


def enteremail():
    x = input("Enter email: ")
    if emailvalidator(x):
        return x
    else:
        return enteremail()


def emailvalidator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False

# <======================= Password =======================>


def enterPassword():
    x = input("Enter Password: ")
    if (len(x) < 8 or not x):
        return enterPassword()
    else:
        Confirmed_password = Confirm_password(x)
        if Confirmed_password:
            return x
        else:
            return enterPassword()


def Confirm_password(Password):
    x = input("Enter Password Again: ")
    if (Password == x or not x):
        return True
    else:
        return False

# <======================= Mobile =======================>


def enterPhone():
    x = input("Enter Your Phone: ")
    if (re.match(r"^01[0-2,5]\d{1,8}$", x)):
        return x
    else:
        return enterPhone()

# <======================= Save Data =======================>


def saveData(data):
    file = open('usersdata.txt', 'a')
    file.writelines(data)
    file.close


def Registration():
    FirstName = enterFName()
    secondName = enterSName()
    email = enteremail()
    Password = enterPassword()
    phone = enterPhone()
    id = round(time.time())
    data = f"{id}:{email}:{Password}:{FirstName}:{secondName}:{phone}\n"
    saveData(data)


def checkExistans(email, password):
    file = open("usersdata.txt", "r")
    data = file.readlines()
    for i in data:
        d = i.split(":")
        if (d[1] == email and d[2] == password):
            return d[0]
    return Login()


def Login():
    print("---------Login------------")
    email = input("email : ")
    password = input("Password: ")
    user_id = checkExistans(email, password)
    mainPage(user_id)


def entryPage():
    print("""============ Welcome Crowd-Funding Entry Page =========== 
    1) Registration
    2) Login """)
    choice = entryInputValidation()
    if (choice == 1):
        Registration()
    elif (choice == 2):
        Login()
