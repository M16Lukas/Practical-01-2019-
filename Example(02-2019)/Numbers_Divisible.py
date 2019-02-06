"""
source : Python Program to Find Numbers Divisible by Another Number (by " www.programiz.com ")
date : 06-02-2019
"""
my_list = [12, 50, 30, 45, 55, 60, 99, 57]

# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), my_list))

# display
print("Numbers divisible by 15 are ", result)
