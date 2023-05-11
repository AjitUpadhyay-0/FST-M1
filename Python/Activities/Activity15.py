"""Handling Errors
Activity 15
Write a Python program that throws a NameError.
Handle the error so it doesn't halt execution."""
try:
    #x=10
    print(x)
except NameError:
    print("x is not there.")