from typing import ValuesView


try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")
    # print(e)
except ZeroDivisionError as e:
    print("Make sure the number is not divisible by 0")
    # print(e)


print("Thanks for using this code")
