# Python Program to Find the Sum of Natural Numbers

num = int(input("Enter a number : "))

if num < 0:
    print("it isn't positive number")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print("The sum is", sum)
