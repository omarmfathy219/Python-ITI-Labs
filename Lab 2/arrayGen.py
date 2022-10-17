# Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.
def arrayGen(length, start):
    array = []
    for i in range(start, length+1, 1):
            array.append(i)
    return array
inputLength = int(input("Enter the length of the array: "))
inputStart = int(input("Enter the start of the array: "))
print(arrayGen(inputLength, inputStart))

arrayGen(inputLength, inputStart)