def main():
    print("Variables in Python.")
    # int
    # float: decimal
    # bool
    # string
    
    # variable is like a box that holds value
    
    j = 14 # Python gives this type int
    x = -2.3 
    yo_world = "Hi"
    statement = True
    # point of variables is that they can change
    # multi-world variables use snake_case
    # this works but don't do this: statement = "I hate python" -> dynamic typing
    print(j)
    print(x)
    print(yo_world)
    print(statement)
    print(j, x, yo_world, statement)
    
    print(type(statement))
    
    # some languages don't like you combining. variables fo different types with operations
    print(x*j) # Python is happy :) -> not possible for computer to store every imaginable number 
    print(type(x*j)) 
    print(14/3) # 4.666666666666667
    print(14//3) # integer division (prints 4) throws out remainder 
    print (14%3)
    print(14**3) # 14 to the power of 3
    
if __name__ == "__main__": # why double underscore
    main()