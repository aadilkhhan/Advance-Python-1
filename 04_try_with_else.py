try:
    i = int(input("Enter the number : "))

    c = 1/i

except Exception as e:
    print(e)

else:
    print("We were successful")