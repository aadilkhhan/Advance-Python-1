a = [3 , 4, 5 , 6 , 7 , 8 , 9 , 23 , 55 , 34 ,245 , 121]
b = []

# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b)

# Short cut write the same
b = [i for i in a if i%2==0]

print(b)

t = [1 , 4 ,75 , 1 ,4 , 5 ,6 , 75]
s = {i for i in t}

print(s)
