# Write a program which repeatedly reads numbers until the user enters “done”.
# ○ Once “done” is entered, print out the total, count, and average of the numbers.
# ○ If the user enters anything other than a number, detect their mistake, print an error message and skip to the next number.
def doneFunc():
    count = 0
    total = 0
    while True:
        number = input("Please Enter a Number: ")
        if (number.isdigit()):
            count += 1
            total += int(number)
        elif (number == "done"):
            break
        else: 
            print("Try Again")
    print(f"The sum of number is:{total} \n  The count of number you enterted is:{count} \n  The average of number is:{total /count}")

doneFunc()
