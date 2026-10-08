#!/usr/bin/env python3

firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))

multiplying = firstnumber * secondnumber

print(firstnumber, "x", secondnumber, "=", multiplying)

if multiplying < 0:
    print("The result is negative.")
elif multiplying > 0:
    print("The result is positive.")
else:
    print("The result is zero.")