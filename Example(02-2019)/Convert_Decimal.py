"""
source : Python Program to Convert Decimal to Binary, Octal and Hexadecimal (by " www.programiz.com ")
date : 06-02-2019
"""
dec = int(input("decimal number : "))

print("The decimal value of", dec, "is:")
print(bin(dec), "is binary")    # '0b' is considered binary
print(oct(dec), "is octal")     # '0o' is considered octal
print(hex(dec), "is hexadecimal")   # '0x' is considered hexadecimal

