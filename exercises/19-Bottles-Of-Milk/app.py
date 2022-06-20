def number_of_bottles():
    for num in range(99, 0, -1):
        print (f"""{num} bottle{"s" if num > 1 else ""} of milk on the wall, {num} bottle{"s" if num > 1 else ""} of milk. Take one down and pass it around, {num-1 if num != 1 else "no more"} bottle{"s" if num-1 != 1 else ""} of milk on the wall.""")
    print("""No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.""")
    return "fyu"


    

number_of_bottles()

