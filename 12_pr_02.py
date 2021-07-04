list1 = ["Zero" , "One" , "Two" , "Three" , "Fourth" , "Fifth" ,  "Sixth" , "seventh"]



for index , item in  enumerate(list1):
    if index == 3  :
        # print(index , item)
        print(f"The {index}rd elemnt is {item}")
    if index == 5 or index == 7:
        print(f"The {index}th elemnt is {item}")
    
    
