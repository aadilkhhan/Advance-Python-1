try:
    i = int(input("Enter the number : "))

    c = 1/i

except Exception as e:
    print(e)

finally:
    print("We are done")

print("Thanls for using the program")