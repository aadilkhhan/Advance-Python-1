a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))

# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Make sure 0 is not divisible by any number")

try :
    print(a/b)
except:
    print("Infinite")