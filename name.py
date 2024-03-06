#!/usr/bin/env
name=input("Enter your name : ")
print("Hello",name)
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")