# write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"
def divFunc(num):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif (num%3 == 0):
        print('Fizz')
    elif (num % 5 == 0):
        print("buzz")
inputNumber = int(input("Enter number: "))

divFunc(inputNumber)