# Python Program to Print the Fibonacci sequence


def Fibonacci(selectedNumber):
    n0 = 0
    n1 = 1
    count = 0

    if selectedNumber <= 0:
        print("it isn't Fibonacci sequence")
    elif selectedNumber == 1:
        print(selectedNumber, "is possible to Fibonacci sequence")
        print(n0)
    else:
        print(selectedNumber, "is possible to Fibonacci sequence")
        while count < selectedNumber:
            print(n0, end=", ")
            total = n0 + n1
            n0 = n1
            n1 = total
            count += 1


number = int(input("select Number : "))
Fibonacci(number)
