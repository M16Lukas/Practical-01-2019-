# Python Program To Display Powers of 2 Using Anonymous Function

terms = int(input("How many terms? "))

result = list(map(lambda x: pow(2, x), range(terms)))

print("The total terms is", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])
