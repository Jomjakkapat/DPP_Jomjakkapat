#!/usr/bin/env python3

number = int(input("Enter a number: "))

if number >25:
    print("Error")
else:
 while number <= 25:
    print("inside the loop, my variable is",number)
    number += 1